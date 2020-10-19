from app import db

class Color(db.Model):
    __tablename__     = "colors"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color             = db.Column(db.String(50))
    activate          = db.Column(db.Boolean, default=True)

def __init__(self, color, activate=True):
    self.color        = color 
    self.activate     = activate     

