from flask import Flask, jsonify, request

app = Flask(__name__)

class Freight:
    def __init__(self, base_price, per_km_price):
        self.base_price = base_price
        self.per_km_price = per_km_price

    def calculate(self, distance_km):
        return self.base_price + (self.per_km_price * distance_km)

# Instância com valores fictícios
freight_service = Freight(base_price=10.0, per_km_price=2.0)

@app.route("/frete", methods=["POST"])
def calculate_freight():
    data = request.get_json()
    distance = data.get("distance")
    if distance is None:
        return jsonify({"error": "Distância não fornecida"}), 400
    cost = freight_service.calculate(distance)
    return jsonify({"distance_km": distance, "freight_cost": cost})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)