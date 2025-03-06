from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Microserviço rodando!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

# Novo endpoint /info
@app.route('/info')
def info():
    return jsonify({
        "nome": "Meu Microserviço",
        "versao": "1.0.0",
        "descricao": "Um microserviço simples usando Flask e Docker",
        "autor": "Bruno Pinheiro",
        "ambiente": "Aula - Cloud Developer"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)