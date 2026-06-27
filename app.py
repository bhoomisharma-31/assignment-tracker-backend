from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Working Successfully"
    })

@app.route("/submit", methods=["POST"])
def submit():

    data = request.json

    assignment = data.get("assignment")

    return jsonify({
        "status": "success",
        "assignment": assignment
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)