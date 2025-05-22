from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

PEDIDOS_FILE = "pedidos.json"

def guardar_pedido(pedido):
    if os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, "r", encoding="utf-8") as f:
            pedidos = json.load(f)
    else:
        pedidos = []
    pedidos.append(pedido)
    with open(PEDIDOS_FILE, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=2)

@app.route("/api/pedidos", methods=["POST"])
def recibir_pedido():
    data = request.json
    guardar_pedido(data)
    return jsonify({"mensaje": "Pedido recibido correctamente"}), 201

@app.route("/api/pedidos", methods=["GET"])
def listar_pedidos():
    if os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, "r", encoding="utf-8") as f:
            pedidos = json.load(f)
    else:
        pedidos = []
    return jsonify(pedidos)

if __name__ == "__main__":
    app.run(debug=True, port=5000) 