
# Pagamentos Service

Este é o microserviço de Formas de Pagamento do projeto de e-commerce. Ele permite o cadastro de formas de pagamento, a realização de pagamentos e a visualização do histórico de transações.

## Funcionalidades

- Cadastro de formas de pagamento (cartão de crédito, boleto, PIX).
- Integração fictícia com gateways de pagamento (ex: Stripe, PagSeguro).
- Histórico de transações.
  
## Requisitos

- Python 3.7+
- Flask

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/CodeCaman/cloud-developer-2TCNPZ.git
    git checkout feature/pagamentos
    cd projetos/e-commerce/pagamentos-service
    ```


## Como Rodar Localmente
1. Certifique-se de ter o Python e o Flask instalados.
   
2. Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
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
    docker build -t pagamentos-service .
    ```
3. Execute o container:
    ```sh
    docker run -p 8181:8181 pagamentos-service
    ```
4. O serviço estará disponível em `http://0.0.0.0:8181`.


## Endpoints

### `GET /`

Renderiza a página inicial com os formulários para cadastro de formas de pagamento e realização de pagamentos.

### `POST /`

Realiza um pagamento com base nos dados fornecidos no formulário. Os tipos de pagamento suportados são:

- Cartão de Crédito
- Boleto
- PIX

### `GET /status`

Retorna o status do serviço.

### `GET /formas_pagamento`

Retorna a lista de formas de pagamento cadastradas.

### `POST /formas_pagamento`

Cadastra uma nova forma de pagamento.

### `GET /historico`

Retorna o histórico de transações realizadas.


## Exemplos de Requisições e Respostas

### Cadastro de Forma de Pagamento

**Requisição:**
```sh
curl -X POST -d "forma_pagamento=Cartão de Crédito" http://0.0.0.0:8181/formas_pagamento
```

**Resposta:**
```json
{
    "message": "Forma de pagamento cadastrada com sucesso",
    "formas_pagamento": ["Cartão de Crédito"]
}
```

### Realização de Pagamento com Cartão de Crédito

**Requisição:**
```sh
curl -X POST -d "cartao=1234567890123456" http://0.0.0.0:8181/
```

**Resposta:**
```json
{
    "data": {
        "cartao_credito": {
            "id": "ch_1Example",
            "amount": 1000,
            "currency": "brl",
            "description": "Pagamento com cartão de crédito",
            "status": "succeeded"
        }
    }
}
```

### Realização de Pagamento com Boleto

**Requisição:**
```sh
curl -X POST -d "boleto=1234567890" http://0.0.0.0:8181/
```

**Resposta:**
```json
{
    "data": {
        "boleto": {
            "payment_url": "https://pagseguro.uol.com.br/checkout/payment/boleto/1234567890"
        }
    }
}
```

### Realização de Pagamento com PIX

**Requisição:**
```sh
curl -X POST -d "pix=0987654321" http://0.0.0.0:8181/
```

**Resposta:**
```json
{
    "data": {
        "pix": {
            "payment_url": "https://pagseguro.uol.com.br/checkout/payment/pix/0987654321"
        }
    }
}
```

### Verificar Status do Serviço

**Requisição:**
```sh
curl http://0.0.0.0:8181/status
```

**Resposta:**
```json
{
    "status": "ok"
}
```

### Ver Histórico de Transações

**Requisição:**
```sh
curl http://0.0.0.0:8181/historico
```

**Resposta:**
```json
{
    "historico": [
        {
            "tipo": "cartao_credito",
            "detalhes": {
                "id": "ch_1Example",
                "amount": 1000,
                "currency": "brl",
                "description": "Pagamento com cartão de crédito",
                "status": "succeeded"
            }
        },
        {
            "tipo": "boleto",
            "detalhes": {
                "payment_url": "https://pagseguro.uol.com.br/checkout/payment/boleto/1234567890"
            }
        },
        {
            "tipo": "pix",
            "detalhes": {
                "payment_url": "https://pagseguro.uol.com.br/checkout/payment/pix/0987654321"
            }
        }
    ]
}
```