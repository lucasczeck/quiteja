# QuitejA

<p align="center">
  <img src="https://via.placeholder.com/150" alt="QuitejA Logo" width="150" height="150">
</p>

<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#requisitos">Requisitos</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#uso">Uso</a> •
  <a href="#api">API</a> •
  <a href="#contribuição">Contribuição</a> •
  <a href="#licença">Licença</a>
</p>

## Sobre

QuitejA é um projeto que [breve descrição do projeto]. Este README fornece instruções para configurar e executar o projeto.

## Requisitos

- Python 3.11
- Git

## Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/lucasczeck/quiteja.git
cd quiteja
```

### 2. Selecione a Branch Master

```bash
git checkout master
```

### 3. Crie um Ambiente Virtual

```bash
python3.11 -m venv venv
```

Ative o ambiente virtual:

- Windows:
  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

## Uso

### 1. Execute o Script de Processamento

```bash
python scripts/script.py
```

### 2. Inicie a API Flask

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000/`.

## API

### Endpoint: `/tipo/<id>`

Retorna informações sobre um tipo específico.

**Método:** GET

**URL:** `http://127.0.0.1:5000/tipo/<id>`

**Exemplo de Resposta:**

```json
{
  "id": 1,
  "nome": "Tipo Exemplo"
}
```

## Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) para mais detalhes.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

<p align="center">
  Desenvolvido com ❤️ por [Seu Nome/Organização]
</p>
