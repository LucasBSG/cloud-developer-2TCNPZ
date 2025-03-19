## Descrição

Este é um microserviço desenvolvido em Python usando Flask para calcular orçamentos. Ele permite calcular o valor total de um orçamento com base no valor unitário de um item, quantidade e um possível desconto.


## Funcionalidades

- Cálculo de orçamentos baseado no custo unitário e quantidade.
- Aplicação de um desconto percentual (opcional).
- API para calcular o orçamento e retornar o valor total.

## Estrutura do Código

- **calculate_budget**: Função responsável pelo cálculo do orçamento, considerando o custo unitário, a quantidade e o desconto.
- **/calculate_budget**: Endpoint da API para receber os parâmetros `cost`, `quantity` e `discount` e retornar o valor total do orçamento.
- **app.py**: Arquivo principal que contém a lógica do cálculo e configura o servidor Flask.

## Como Executar

- Rodando localmente

- Instale as dependências:

'''
pip install flask
'''

Execute o aplicativo:

python app.py

- Faça uma requisição:

curl "http://localhost:5003/calculate_budget?cost=100&quantity=5&discount=10"

- Rodando com Docker

Construa a imagem Docker:

'''
docker build -t orcamento-services .
'''

Execute o contêiner:

'''
docker run -d -p 5003:5003 --name microservico orcamento-services
'''

## Exemplo de Uso

Para calcular um orçamento de 5 itens com preço unitário de 100 e um desconto de 10%, a requisição seria:
curl "http://localhost:5003/calculate_budget?cost=100&quantity=5&discount=10"

http://localhost:5003/calculate_budget?cost=100&quantity=5&discount=10


Se o cálculo for bem-sucedido, a resposta será:

{
  "total": 450.0
}

Caso algum parâmetro esteja incorreto ou ausente, a resposta será um erro:

{
  "error": "missing parameter 'cost'"
}