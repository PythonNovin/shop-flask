import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token

def jwt_config(app):
    
    load_dotenv()
    
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")

    JWTManager(app)
    
    return app

def jwt_create(id):
    return create_access_token(identity=id)
