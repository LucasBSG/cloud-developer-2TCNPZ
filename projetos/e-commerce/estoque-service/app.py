from flask import Flask, jsonify
import random

app = Flask(__name__)

# Lista de produtos
produtos = [
    {"id": 1, "nome": "Produto A", "preco": 10.99},
    {"id": 2, "nome": "Produto B", "preco": 20.99},
    {"id": 3, "nome": "Produto C", "preco": 30.99},
    {"id": 4, "nome": "Produto D", "preco": 40.99},
    {"id": 5, "nome": "Produto E", "preco": 50.99}
]

@app.route('/')
def home():
    return "estoque-service ok!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/estoque')
def estoque():
    # Seleciona 3 produtos aleatórios da lista
    produtos_selecionados = random.sample(produtos, 5)
    return jsonify(produtos_selecionados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)