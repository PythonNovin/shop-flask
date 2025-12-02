from mongoengine import Document, StringField, FloatField

class User(Document):
    name = StringField(required = True)
    phone = StringField(required = True, unique = True)
    email = StringField(required = False)
    password = StringField(required = True)
    postal_code = StringField(required = False)
    address = StringField(required = False)
    money = FloatField(required = True, default = 0)
    bank = StringField(required = False)
    
    meta = {
        "collection" : "Users",
        "indexer" : [
            {"fields" : ["phone"], "unique":True},
        ]
    }