from flask import jsonify

from models.User import User
from utils.validation import *
from utils.hash import hash_password

def register(data):
    try:
        phone = data.get("phone")
        password = data.get("password")
        
        if not phone or not password :
            return jsonify({
                "message" : "phone and password is required",
                "result" : None
            }), 400
        
        if isvalid_phone(phone):
            return jsonify({
                "message" : "phone invalid",
                "result" : None
            }), 400
            
        if isvalid_password(password):
            return jsonify({
                "message" : "password invalid",
                "result" : None
            }), 400 
        
        password = hash_password(password)
        
        new_user = {
            "phone" : phone,
            "password" : password,
            "name" : "",
            "postal_code" : "",
            "address" : "",
            "money" : 0,
            "bank" : "",
            "email" : ""
        }
        
        User(**new_user).save()
        
        return jsonify({
                "message" : "Registered successfuly",
                "result" : new_user
            }), 201
    except:
        return jsonify({
                "message" : "Faild",
                "result" : None
            }), 500