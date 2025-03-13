# Lojas Service

Este é o microserviço de Lojas do projeto de e-commerce. Ele permite o cadastro de lojas, a associação de produtos a lojas, e fornece um dashboard para visualização de vendas e estoque.

## Funcionalidades

- Cadastro de lojas (nome, descrição, endereço, contato).
- Associação de produtos a lojas.
- Dashboard para lojas visualizarem vendas e estoque.
- Histórico de lojas e produtos associados.

## Requisitos

- Python 3.7+
- Flask

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/CodeCaman/cloud-developer-2TCNPZ.git
    cd cloud-developer-2TCNPZ
    git checkout feature/lojas
    cd projetos/e-commerce/lojas-service
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
5. O serviço estará disponível em `http://0.0.0.0:8282`.

## Como Rodar com Docker

1. Certifique-se de ter o Docker instalado.
2. Construa a imagem Docker:
    ```sh
    docker build -t lojas-service .
    ```
3. Execute o container:
    ```sh
    docker run --name lojas-service-container -p 8282:8282 lojas-service lojas-service
    ```
4. O serviço estará disponível em `http://0.0.0.0:8282`.

## Endpoints

### `POST /lojas`

Cadastra uma nova loja.

**Parâmetros:**
- `nome` (string): Nome da loja.
- `descricao` (string): Descrição da loja.
- `endereco` (string): Endereço da loja.
- `contato` (string): Contato da loja.

**Exemplo de Requisição:**
```sh
curl -X POST http://localhost:8282/lojas -d "nome=Loja A&descricao=Descrição da Loja A&endereco=Endereço da Loja A&contato=Contato da Loja A"

**Exemplo de Resposta:**
```json
{
  "message": "Loja cadastrada com sucesso",
  "loja_id": 1,
  "lojas": [
    {
      "id": 1,
      "nome": "Loja A",
      "descricao": "Descrição da Loja A",
      "endereco": "Endereço da Loja A",
      "contato": "Contato da Loja A"
    }
  ]
}
```

### `POST /produtos_lojas`

Associa um produto a uma loja.

**Parâmetros:**
- `loja_id` (int): ID da loja.
- `produto_id` (int): ID do produto.

**Exemplo de Requisição:**
```sh
curl -X POST http://localhost:8282/produtos_lojas -d "loja_id=1&produto_id=101"
```

**Exemplo de Resposta:**
```json
{
  "message": "Produto 101 associado à loja 1 com sucesso",
  "produtos_lojas": [
    {
      "loja_id": 1,
      "produto_id": 101
    }
  ]
}
```

### `GET /dashboard/<int:loja_id>`

Retorna o dashboard de vendas e estoque de uma loja.

**Parâmetros:** `loja_id` (int): ID da loja.

**Exemplo de Requisição:**
```sh
curl http://localhost:8282/dashboard/1
```

**Exemplo de Resposta:**
```json
{
  "vendas": [],
  "estoque": [
    {
      "loja_id": 1,
      "produto_id": 101
    }
  ]
}
```

### `GET /historico`

Retorna o histórico de lojas e produtos associados.

**Exemplo de Requisição:**
```sh
curl http://localhost:8282/historico
```

**Exemplo de Resposta:**
```json
{
  "total_lojas": 1,
  "total_produtos_associados": 1
}
```

### `GET /status`

Retorna o status do serviço.

**Exemplo de Requisição:**
```sh
curl http://localhost:8282/status
```

**Exemplo de Resposta:**
```json
{
  "status": "ok"
}
```

## Exemplos de Requisições e Respostas

### Cadastro de Loja

**Requisição:**
```sh
curl -X POST http://localhost:8282/lojas -d "nome=Loja A&descricao=Descrição da Loja A&endereco=Endereço da Loja A&contato=Contato da Loja A"
```

**Resposta:**
```json
{
  "message": "Loja cadastrada com sucesso",
  "loja_id": 1,
  "lojas": [
    {
      "id": 1,
      "nome": "Loja A",
      "descricao": "Descrição da Loja A",
      "endereco": "Endereço da Loja A",
      "contato": "Contato da Loja A"
    }
  ]
}
```

### Associação de Produto a Loja

**Requisição:**
```sh
curl -X POST http://localhost:8282/produtos_lojas -d "loja_id=1&produto_id=101"
```

**Resposta:**
```json
{
  "message": "Produto 101 associado à loja 1 com sucesso",
  "produtos_lojas": [
    {
      "loja_id": 1,
      "produto_id": 101
    }
  ]
}
```

### Dashboard

**Requisição:**
```sh
curl http://localhost:8282/dashboard/1
```

**Resposta:**
```json
{
  "vendas": [],
  "estoque": [
    {
      "loja_id": 1,
      "produto_id": 101
    }
  ]
}
```

### Histórico

**Requisição:**
```sh
curl http://localhost:8282/historico
```

**Resposta:**
```json
{
  "total_lojas": 1,
  "total_produtos_associados": 1
}
```

### Verificar Status do Serviço

**Requisição:**
```sh
curl http://localhost:8282/status
```

**Resposta:**
```json
{
  "status": "ok"
}
```