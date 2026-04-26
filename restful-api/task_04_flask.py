#!/usr/bin/python3
"""This module contains restful-api tasks."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def return_users():
    return jsonify(users)


@app.route("/status")
def check_status():
    return "OK"


@app.route("/users/<username>")
def return_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Invalid data"}), 400

    username = data["username"]

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
