## Descrição

Este é um microserviço desenvolvido em Python usando Flask para calcular o custo de frete com base na distância informada pelo usuário.

## Funcionalidades

- Cálculo do frete com base em uma taxa fixa e um valor por quilômetro.

- API para receber requisições e retornar o custo do frete.

## Estrutura do Código

- Freight: Classe que define as regras de cálculo do frete.

- freight_service: Instância da classe Freight com valores fictícios.

- calculate_freight(): Endpoint que recebe a distância e retorna o custo do frete.

## Como Executar

- Rodando localmente

- Instale as dependências:

'''
pip install flask
'''

Execute o aplicativo:

python app.py

- Faça uma requisição para calcular o frete:

curl -X POST http://localhost:5002/frete -H "Content-Type: application/json" -d '{"distance": 100}'

- Rodando com Docker

Construa a imagem Docker:

'''
docker build -t frete-services .
'''

Execute o contêiner:

'''
docker run -d -p 5002:5002 --name microservico frete-services
'''

## Exemplo de Uso

Se a distância for 100 km, a API retornará:

{
  "distance_km": 100,
  "freight_cost": 210.0
}