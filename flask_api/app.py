
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Medicine Redistribution API is running!"

@app.route("/api/transfer-plan", methods=["POST"])
def transfer_plan():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({
            "error": "Please send valid JSON inventory data"
        }), 400

    # Temporary response until the real backend is connected
    return jsonify({
        "status": "success",
        "message": "Inventory received successfully",
        "received_data": data
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
