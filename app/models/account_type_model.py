from app import db

class AccountType(db.Model):
    __tablename__    = "account_types"
    id               = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name             = db.Column(db.String(150))
    icon_id          = db.Column(db.Integer, db.ForeignKey('icons.id'))
    activate         = db.Column(db.Boolean, default=True)
    
    icon             = db.relationship("Icon", lazy='joined')

def __init__(self, name, icon_id, activate=True):
    self.name             = name  
    self.icon_id          = icon_id 
    self.activate         = activate        

