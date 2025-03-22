# Clientes Service

Este projeto é um serviço de cadastro de clientes desenvolvido com Flask. Ele permite que os usuários cadastrem novos clientes através de um formulário web.

## Funcionalidades

- **Cadastro de Clientes**: A rota principal (`/`) exibe um formulário onde os usuários podem inserir o nome e o email de um cliente. Ao enviar o formulário, os dados são processados e uma mensagem de sucesso é retornada.
- **Status do Serviço**: A rota `/status` retorna um JSON indicando que o serviço está funcionando corretamente.
- **Informações do Serviço**: A rota `/info` retorna um JSON com informações adicionais sobre o serviço.

## Rotas

- `GET /`: Exibe o formulário de cadastro de clientes.
- `POST /`: Processa os dados do formulário de cadastro de clientes e retorna uma mensagem de sucesso.
- `GET /status`: Retorna o status do serviço.
- `GET /info`: Retorna informações adicionais sobre o serviço.

## Como Executar

1. Certifique-se de ter o Python e o Flask instalados.
2. Execute o comando `python app.py` para iniciar o servidor Flask.
3. Acesse `http://localhost:8080` no seu navegador para visualizar o formulário de cadastro de clientes.

## Exemplo de Uso

1. Acesse `http://localhost:8080`.
2. Preencha o formulário com o nome e o email do cliente.
3. Clique em "Cadastrar" para enviar os dados.
4. Uma mensagem de sucesso será exibida com os dados do cliente cadastrado.

## Estrutura do Projeto

- `app.py`: Contém a lógica principal do serviço, incluindo as rotas e o processamento dos dados do formulário.
- `README.md`: Este arquivo, contendo a descrição do projeto e instruções de uso.

## Dependências

- Flask

## Instalação

Para instalar as dependências, execute:

```bash
pip install flask