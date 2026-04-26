#!/usr/bin/python3
"""Flask API"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# ВАЖНО: изначально пусто
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(users)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Проверка на наличие username
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Проверка на дубликат
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Добавление пользователя
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added"}), 201


if __name__ == "__main__":
    app.run()
