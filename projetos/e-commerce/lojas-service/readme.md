
# Lojas Service

Este é o microserviço de lojas do projeto de e-commerce. Ele permite o cadastro de Lojas.

## Funcionalidades

- Cadastro de lojas (nome, descrição, endereço, contato).
- Associação de produtos a lojas.
- Dashboard para lojas visualizarem vendas e estoque.
  
## Requisitos

- Python 3.7+
- Flask

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/CodeCaman/cloud-developer-2TCNPZ.git
    git checkout feature/lojas
    cd projetos/e-commerce/lojas-service
    ```


## Como Rodar Localmente
1. Certifique-se de ter o Python e o Flask instalados.
   
2. Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Execute o serviço:
    ```sh
    python app.py
    ```
5. O serviço estará disponível em `http://0.0.0.0:8181`.

## Como Rodar com Docker

1. Certifique-se de ter o Docker instalado.
2. Construa a imagem Docker:
    ```sh
    docker build -t lojas-service .
    ```
3. Execute o container:
    ```sh
    docker run --name lojas-service-container -p 8181:8181 lojas-service
    ```
4. O serviço estará disponível em `http://0.0.0.0:8181`.


## Endpoints

### `GET /`

Renderiza a página inicial com os formulários para cadastro de lojas.


### `GET /status`

Retorna o status do serviço.



## Exemplos de Requisições e Respostas

