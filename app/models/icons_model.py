from app import db

class Icon(db.Model):
    __tablename__     = "icons"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    icon              = db.Column(db.String(50))
    activate          = db.Column(db.Boolean, default=True)

def __init__(self, icon, activate=True):
    self.icon        = icon      
    self.activate    = activate

