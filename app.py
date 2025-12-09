import os
from flask import Flask
from mongoengine import connect

from utils.jwt import jwt_config

connect(db="shop", host="mongodb://localhost:27017/shop")

app = Flask(__name__)

from routes import *

app = jwt_config(app)

if __name__ == "__main__":
    app.run(debug=True)