from app import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), index=True, unique=True)
    short_url = db.Column(db.String(100), unique=True)
