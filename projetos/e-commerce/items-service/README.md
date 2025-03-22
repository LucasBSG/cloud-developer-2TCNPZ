# Módulo de Itens 

Este é o microserviço de Itens do projeto de e-commerce. Ele permite o cadastro de itens, a visualização dos itens cadastrados e a atualização ou remoção de itens.

## Funcionalidades 

- Cadastro de itens (nome, descrição, preço).
- Visualização dos itens cadastrados.
- Atualização e remoção de itens.

## Requisitos

- Python 3.7+
- Flask

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/CodeCaman/cloud-developer-2TCNPZ.git
    cd cloud-developer-2TCNPZ
    git checkout feature/items
    cd projetos/e-commerce/items-service
    ```

## Como Rodar Localmente

1. Certifique-se de ter o Python e o Flask instalados.
   
2. Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv\Scripts\activate
    ou
    .\venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Execute o serviço:
    ```sh
    python app.py
    ```
5. O serviço estará disponível em `http://0.0.0.0:8383`.

## Como Rodar com Docker

1. Certifique-se de ter o Docker instalado.
2. Construa a imagem Docker:
    ```sh
    docker build -t items-service .
    ```
3. Execute o container:
    ```sh
    docker run --name items-service-container -p 8383:8383 items-service
    ```
4. O serviço estará disponível em `http://0.0.0.0:8383`.

## Endpoints

### `GET /`

Renderiza a página inicial com o formulário para cadastro de itens e a lista de itens cadastrados.

### `POST /itens`

Cadastra um novo item com base nos dados fornecidos no formulário.

### `GET /itens`

Retorna a lista de itens cadastrados.

### `GET /itens/<int:item_id>`

Retorna os detalhes de um item específico.

### `PUT /itens/<int:item_id>`

Atualiza os dados de um item específico.

### `DELETE /itens/<int:item_id>`

Remove um item específico.

### `GET /status`

Retorna o status do serviço.

## Exemplos de Requisições e Respostas

### Cadastro de Item

**Requisição:**
```sh
curl -X POST -d "nome=Item1&descricao=Descrição do Item1&preco=10.00" http://0.0.0.0:8383/itens