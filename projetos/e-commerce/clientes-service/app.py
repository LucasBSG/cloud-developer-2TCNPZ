from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        # Aqui você pode adicionar a lógica para salvar o cliente no banco de dados
        return jsonify({"message": f"Cliente '{nome}' com email '{email}' cadastrado com sucesso!"})
    return render_template_string('''
        <h1>Cadastro de Clientes</h1>
        <form method="post">
            Nome: <input type="text" name="nome">
            Email: <input type="text" name="email">
            <input type="submit" value="Cadastrar">
        </form>
    ''')

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)