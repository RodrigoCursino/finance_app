from app import db

class Bank(db.Model):
    __tablename__     = "banks"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column(db.String(150))
    code              = db.Column(db.String(4))
    brand             = db.Column(db.String(300))
    activate          = db.Column(db.Boolean, default=True)

def __init__(self, name, code, brand, activate=True):
    self.name        = name 
    self.code        = code
    self.brand       = brand
    self.activate    = activate     

