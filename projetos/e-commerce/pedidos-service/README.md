# Módulo de Pedidos 🛒

Este projeto é um serviço de cadastro de pedidos desenvolvido com Flask. Ele permite que os pedidos sejam cadastrados com nome do produto, nome do cliente e forma de pagamento 💳

## Funcionalidades ✨

- *Cadastro de pedidos* 📝: A rota principal (/) exibe um formulário onde os usuários podem inserir o nome do produto, nome do cliente e a forma de pagamento. Ao enviar o formulário, os dados são processados e uma mensagem de sucesso é retornada.
- *Status do Serviço* 🟢: A rota /status retorna um JSON indicando que o serviço está funcionando corretamente.

## Rotas 🔄

- GET /: Exibe o formulário de cadastro de pedidos.
- POST /: Processa os dados do formulário e retorna uma mensagem de sucesso.
- GET /status: Retorna o status do serviço.

## Como Executar ▶️

1. Certifique-se de ter o Python 🐍 e o Flask instalados.
2. Execute o comando `python app.py` para iniciar o servidor Flask.
3. Acesse http://localhost:8080 no seu navegador para visualizar o formulário de cadastro de pedidos.

## Exemplo de Uso 🔍

1. Acesse http://localhost:8080.
2. Preencha o formulário com o nome do produto, nome do cliente e forma de pagamento.
3. Clique em "Enviar" para enviar os dados.
4. Uma mensagem de sucesso será exibida com os dados do pedido cadastrado ✅.

## Estrutura do Projeto 📁

- app.py: Contém a lógica principal do serviço, incluindo as rotas e o processamento dos dados do formulário.
- README.md: Este arquivo, contendo a descrição do projeto e instruções de uso.

## Dependências 📦

- blinker==1.9.0
- click==8.1.8
- colorama==0.4.6
- Flask==3.1.0
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- Werkzeug==3.1.3

## Instalação 🔧

Para instalar as dependências, execute:

```bash
pip install --no-cache-dir -r requirements.txt