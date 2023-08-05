#!/usr/bin/env python3
from flask import Flask, request, jsonify
from typing import Optional


app = Flask(__name__)


db = {
    123: {
        "name": "rod",
        "email": "rod@email.com",
        "phone": 9876543212
    }
}

db_2 = {
    "rod": {
        "id": 1,
        "email": "rod@email.com",
        "phone": 9876543212
    }
}

@app.route("/")
def api_home():
    return "docs"


# http://127.0.0.1:5000/get-item/123
"""
curl -X 'GET' \
  'http://127.0.0.1:5000/get-item/123' \
  -H 'accept: application/json'
"""
@app.route("/get-item/<int:item_id>")
def get_item(item_id):
    if item_id not in db:
        return jsonify({"error": "Item does not exist."}), 404 
    return jsonify(db[item_id]), 200


# http://127.0.0.1:5000/get-by-name/rod
"""
curl -X 'GET' \
  'http://127.0.0.1:5000/get-by-name/rod' \
  -H 'accept: application/json'
"""
@app.route("/get-by-name/<string:name>")
def get_by_name(name: str, item_id: Optional[int]=None):
    if item_id:
        if db_2[name]["id"] == item_id:
            return db_2[name]
        return jsonify({"error": "Name does not exist."}), 404 
    return jsonify(db_2[name]), 200


"""
curl -X 'POST' \
  'http://127.0.0.1:5000/create-item/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "bob",
  "email": "b@c.com",
  "phone": 1234567890
}'
"""
@app.route("/create-item/<int:item_id>", methods=["POST"])
def create_item(item_id: int):
    if item_id in db:
        return jsonify({"error": "Item ID already exists."}), 404
    
    data = request.get_json()
    db[item_id] = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone")
    }
    return jsonify(db[item_id]), 200


"""
curl -X 'PUT' \
  'http://127.0.0.1:5000/update-item/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "bobby",
  "email": "a@r.com",
  "phone": 9887654332
}'
"""
@app.route("/update-item/<int:item_id>", methods=["PUT"])
def update_item(item_id: int):
    if item_id not in db:
        return jsonify({"error": "Item ID does not exist."}), 404 
    
    data = request.get_json()
    db[item_id] = data
    return jsonify(db[item_id]), 200


"""
curl -X 'DELETE' \
  'http://127.0.0.1:5000/delete-item/123' \
  -H 'accept: application/json'
"""
@app.route("/delete-item/<int:item_id>", methods=["DELETE"])
def delete_item(item_id: int):
    if item_id not in db:
        return jsonify({"error": "Item ID does not exist."}), 404 
    
    del db[item_id]
    return jsonify({"data": "{} deleted".format(item_id)}), 200


if __name__ == "__main__":
    app.run(debug=True)
