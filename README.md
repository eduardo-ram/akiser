# Akiser (Aqui Serviços)

Akiser é uma aplicação web para conectar pessoas que oferecem seus serviços com contratantes.

# Funcionalidades

* Cards com imagem, descrição, valor e link de contato (WhatsApp)
* Formulário para cadastrar serviço (nome, serviço, descrição, contato, valor, imagem)
* Dados armazenados em CSV
* Upload de imagem salvo em `app/static/images/`
* Interface responsiva com Bootstrap
* Rodapé com links e lista de serviços
* Página de erro personalizada (404 e 500)
* Tabela com todos os serviços em `/services`

# Tecnologias

* Flask (Python), Jinja2
* Bootstrap 5 (CDN)
* CSV para persistência

# Estrutura

app/
  __init__.py
  main/
    __init__.py
    routes.py
  static/
    css/style.css
    images/
  templates/
    base.html
    index.html
    services.html
    error.html
data/dados.csv
.gitignore
app.py
README.md

# Como rodar

1. Criar e ativar ambiente virtual

     python -m venv venv
     .\venv\Scripts\Activate.ps1

2. Instalar dependências

   pip install flask

3. Executar

   python app.py

4. Acessar
   `http://127.0.0.1:5000`

# CSV

Cabeçalho:

nome,servico,descricao,contato,imagem,valor

# Rotas

* `/` — cards de serviços e formulário de cadastro
* `/services` — tabela com todos os serviços
* Erros: 404 e 500 renderizam `error.html`