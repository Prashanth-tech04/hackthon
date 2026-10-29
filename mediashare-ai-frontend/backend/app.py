
from flask import Flask,request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Flask is running!"

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "Flask is connected!"})


@app.route("/api/transfer-plan", methods=["POST"])
def transfer_plan():
    data = request.get_json(silent=True) or {}

    inventory = data.get("inventory", [])
    facilities = data.get("facilities", [])

    return jsonify({
        "message": "Inventory received by Flask successfully!",
        "inventory_records_received": len(inventory),
        "facilities_received": len(facilities),
        "transfers": []
    })


print("REGISTERED ROUTES:")
print(app.url_map)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
