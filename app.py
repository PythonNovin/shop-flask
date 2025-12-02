from flask import Flask
from mongoengine import connect

connect(db="shop", host="mongodb://localhost:27017/shop")

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)