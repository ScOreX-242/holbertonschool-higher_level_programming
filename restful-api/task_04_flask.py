#!/usr/bin/python3
"""This module contains restful-api tasks."""
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def return_users(): 
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(users)

@app.route("/status")
def check_status():
    return "OK"

@app.route("/users/<username>")
def return_user(username):
    if ()

@app.route("/add_user", methods=['POST'])
def add_user(add_user):
    data = request.get_json()

if __name__ == "__main__":
    app.run()
