from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index=True,  unique=True)
    password = db.Column(db.String(250), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
