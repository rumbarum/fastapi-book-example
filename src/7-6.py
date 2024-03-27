from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hi", methods=["POST"])
def greet():
    who: str = request.json["who"]
    return jsonify(f"Hello? {who}?")


if __name__ == "__main__":
    app.run()
