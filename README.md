# Plataforma de Bug Bounty

## Descrição do Projeto
Este projeto é uma página de uma **Plataforma de Bug Bounty** que conecta empresas e freelancers de segurança para identificar vulnerabilidades em sistemas. A página possui seções para:
- Apresentar a plataforma.
- Exibir empresas participantes.
- Listar regras para submissão de vulnerabilidades.
- Permitir que usuários enviem relatórios detalhados.

## Como Iniciar o Projeto Localmente

### Requisitos
- Navegador moderno (como Chrome ou Firefox).
- Um servidor local para servir os arquivos HTML.

### Métodos de Iniciação

1. Abra a pasta do projeto no **VS Code**.

2.  Crie um ambiente virtual:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Migre o banco de dados:

    ```bash
    python manage.py migrate
    ```

## Como usar

1.  Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

2.  Acesse o aplicativo no seu navegador:

    ```
    http://localhost:8000/
    ```

