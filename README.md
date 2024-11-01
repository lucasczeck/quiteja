QuitejA
Este é o repositório do projeto QuitejA. Siga as instruções abaixo para configurar e executar o projeto.

Requisitos
Python 3.11
Git
Configuração do Projeto
1. Clonar o Repositório
Para clonar o projeto do GitHub, execute o seguinte comando no terminal:

git clone https://github.com/lucasczeck/quiteja.git
cd quiteja
2. Selecionar a Branch Master
Certifique-se de estar na branch master:

git checkout master
3. Criar um Ambiente Virtual
Crie um ambiente virtual usando Python 3.11:

python3.11 -m venv venv
Ative o ambiente virtual:

No Windows:

venv\Scripts\activate
No macOS e Linux:

source venv/bin/activate
4. Instalar as Dependências
Instale as bibliotecas necessárias do arquivo requirements.txt:

pip install -r requirements.txt
Executando o Projeto
1. Executar o Script de Processamento
Para executar o script de processamento, use o seguinte comando:

python scripts/script.py
2. Iniciar a API Flask
Para iniciar a API Flask, execute:

python app.py
A API estará disponível em http://127.0.0.1:5000/.

Fazendo Requisições à API
Para fazer requisições à API, use a rota tipo/<id>. Por exemplo:

http://127.0.0.1:5000/tipo/1
Substitua 1 pelo ID desejado.

Suporte
Se você encontrar algum problema ou tiver dúvidas, por favor, abra uma issue no repositório do GitHub.
