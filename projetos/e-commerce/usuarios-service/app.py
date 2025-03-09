from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para armazenar os usuários
usuarios = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obter dados do usuário do corpo da solicitação
        novo_usuario = request.get_json()
        # Adicionar o novo usuário à lista
        usuarios.append(novo_usuario)
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    return "Microserviço rodando!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/info')
def info():
    return "Nossa aplicação é muito boa e concluimos o desafio 3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)