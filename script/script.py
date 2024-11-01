import zipfile
import pandas as pd
from sqlalchemy import create_engine, text

# Aqui descompacto o arquivo dados.zip para poder acessar os arquivos CSV internos, utilizei uma lib que já conhecia e
# havia utilizado em outros projetos
with zipfile.ZipFile('script/dados.zip', 'r') as zip_ref:
    zip_ref.extractall('script/')

# Faço a leitura dos dados CSV e coloco em dataframes para facilitar o trabalho com eles, utilizando pandas que também
# já conhecia
origem_dados = pd.read_csv('script/origem-dados.csv')
tipos = pd.read_csv('script/tipos.csv')

# Filtro os dados por status
criticos = origem_dados[origem_dados['status'] == 'CRITICO']

# Ordeno os dados filtrados pela coluna 'created_at'
criticos_ordenados = criticos.sort_values('created_at')

# Aqui crio um dicionário a partir do arquivo tipos.csv para mapear os IDs de tipo para seus nomes. Nessa etapa utilizei
# consultas no ChatGPT para encontrar a maneira mais eficiente de criar a coluna e popular os dados
tipos_dict = dict(zip(tipos['id'], tipos['nome']))
criticos_ordenados['nome_tipo'] = criticos_ordenados['tipo'].map(tipos_dict)

# Para cada linha de dados criticos, crio um insert e salvo tudo no arquivo
with open('script/insert-dados.sql', 'w') as f:
    for _, row in criticos_ordenados.iterrows():
        columns = ', '.join(row.index)
        values = ', '.join([f"'{str(value)}'" for value in row.values])
        insert_statement = f"INSERT INTO dados_finais ({columns}) VALUES ({values});\n"
        f.write(insert_statement)

# Utilizei o SQLALchemy para criar um banco de dados local e criar uma tabela com o dataframe descobri que poderia
# fazer isso fazendo pesquisas no ChatGPT
engine = create_engine('sqlite:///dados_finais.db')
criticos_ordenados.to_sql('dados_finais', engine, if_exists='replace', index=False)

# Criação de uma query para buscar registros por tipo e por dia
query = """
SELECT DATE(created_at) as date, nome_tipo, COUNT(*) as count
FROM dados_finais
GROUP BY DATE(created_at), nome_tipo
ORDER BY DATE(created_at), nome_tipo;
"""

# Executando e printando o resultado da query
with engine.connect() as connection:
    result = connection.execute(text(query))
    print("Resultados da query:")
    print("Data | Tipo | Contagem")
    print("-----------------------")
    for row in result:
        print(f"{row.date} | {row.nome_tipo} | {row.count}")
