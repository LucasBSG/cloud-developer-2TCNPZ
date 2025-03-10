from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para calcular o orçamento
def calculate_budget(cost: float, quantity: int, discount: float = 0) -> float:
    """
    Função que calcula o orçamento total com base no custo unitário,
    quantidade e um possível desconto.
    """
    total = cost * quantity
    total_after_discount = total - (total * discount / 100)
    return round(total_after_discount, 2)

# Rota para calcular o orçamento
@app.route('/calculate_budget', methods=['GET'])
def budget():
    try:
        # Pega os parâmetros da requisição
        cost = float(request.args.get('cost'))
        quantity = int(request.args.get('quantity'))
        discount = float(request.args.get('discount', 0))

        # Calcula o total
        total = calculate_budget(cost, quantity, discount)

        # Retorna o total em formato JSON
        return jsonify({"total": total}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Inicializa o servidor Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)