from app import db

class CreditCardBanner(db.Model):
    __tablename__  = "credit_card_flags"
    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name           = db.Column(db.String(150))
    brand          = db.Column(db.String(300))
    activate       = db.Column(db.Boolean, default=True)

def __init__(self, name, brand, activate=True):
    self.name      = name 
    self.brand     = brand
    self.activate  = activate     

