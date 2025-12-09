from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.User import User
from utils.decode_mongo import decode_mongo


from app import app
from .register import register
from .login import login

@app.route("/" , methods=["POST"])
def register_handler():
    data = request.get_json()
    return register(data)

@app.route("/login", methods=["POST"])
def login_handler():
    data = request.get_json()
    return login(data)

@app.route("/<id>", methods=["GET"])
@jwt_required()
def get_data_user_handler(id):
    a = decode_mongo(User.objects(id = get_jwt_identity()))
    return a[0]["phone"]
