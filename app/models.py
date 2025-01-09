from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.interger, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(20), default = "user")


class Food(db.Model):
    id = db.Column(db.interger, primary_key = True)
    name = db.Column(db.String(100) , nullable= False)
    price = db.Column(db.Float , nullale = False)
    category = db.Column(db.String(100), nullable = False)

