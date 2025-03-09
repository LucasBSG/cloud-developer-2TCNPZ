from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome_produto = request.form['nome']
        pagamento = request.form['pagamento']
        cliente = request.form['cliente']
        return jsonify({"data": {"nome_produto": nome_produto, "pagamento": pagamento, "cliente": cliente}})
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)