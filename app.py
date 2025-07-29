"""
Flask Quote Microservice

This simple Flask app serves as a microservice that returns
a random inspirational quote via a `/quote` endpoint.
"""

from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of sample quotes
QUOTES = [
    "Stay hungry, stay foolish. – Steve Jobs",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different. – Coco Chanel",
    "The best way to get started is to quit talking and begin doing."
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Quote Microservice!",
        "usage": "GET /quote to receive a random quote"
    })

@app.route("/quote", methods=["GET"])
def get_quote():
    """
    Returns a random quote in JSON format.
    """
    quote = random.choice(QUOTES)
    return jsonify({"quote": quote})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)