from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Feature permissoes rodando!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/info')
def info():
    return "Nossa aplicação é muito boa e concluimos o microserviço com sucesso!/n Feature permissoes finalizada!"

@app.route('/permissao')
def status():
    return "O usuário tem permissao de acesso as features do projeto"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)