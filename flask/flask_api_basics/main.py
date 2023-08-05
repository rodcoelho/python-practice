from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def api_home():
    return "docs"


@app.route("/get-thing/<thing_id>")
def get_thing(thing_id):
    thing_data = {
        "id": thing_id,
        "name": "it",
        "email": "rod@email.com"
    }

    extra = request.args.get("extra")
    if extra:
        thing_data["extra"] = extra

    return jsonify(thing_data), 200


@app.route("/create-thing/", METHODS=["POST"])
def create_thing():
    data = request.get_json()

    # put_in_db()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
