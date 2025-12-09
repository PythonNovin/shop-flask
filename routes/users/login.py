from flask import jsonify

from models.User import User
from utils.validation import *
from utils.hash import hash_password
from utils.decode_mongo import decode_mongo
from utils.jwt import jwt_create

def login(data):
    try:
        phone = data.get("phone")
        password = data.get("password")
        
        user = decode_mongo(User.objects(phone = phone))
        password = hash_password(password)
        
        if len(user) == 0:
            return jsonify({
                "message" : "phone or password is incorrect",
                "result" : None
            }), 404
            
        if password != user[0]["password"]:
            return jsonify({
                "message" : "phone or password is incorrect",
                "result" : None
            }), 404

        return jsonify({
                "message" : "login successfuly",
                "result" : jwt_create(user[0]["_id"])  
            }), 201
    except:
        return jsonify({
                "message" : "Faild",
                "result" : None
            }), 500