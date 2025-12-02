from flask import request

from app import app
from .register import register

@app.route("/" , methods=["POST"])
def register_handler():
    data = request.get_json()
    return register(data)

@app.route("/login", methods=["POST"])
def login_handler():
    return "ok"

@app.route("/<id>", methods=["GET"])
def get_data_user_handler(id):
    return "ok"