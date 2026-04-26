#!/usr/bin/python3
"""Flask API with Basic Auth and JWT"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT config
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Basic Auth
auth = HTTPBasicAuth()

# Users storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ----------------------
# BASIC AUTH
# ----------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ----------------------
# JWT AUTH
# ----------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(data["username"])

    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # кладём username в токен
    access_token = create_access_token(identity=data["username"])

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ----------------------
# ROLE-BASED ACCESS
# ----------------------
@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)

    if not user or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ----------------------
# JWT ERROR HANDLERS
# ----------------------
@jwt.unauthorized_loader
def unauthorized_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run()
