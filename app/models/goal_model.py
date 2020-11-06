from app                        import db
from datetime                   import datetime
from sqlalchemy.ext.declarative import declarative_base

class Goal(db.Model):
    __tablename__     = "goals"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description       = db.Column(db.String(50))
    total             = db.Column(db.Float(precision=2,asdecimal=True))
    start_date        = db.Column(db.DateTime, default=datetime.utcnow)
    end_date          = db.Column(db.DateTime)
    color_id          = db.Column(db.Integer, db.ForeignKey('colors.id'))
    user_id           = db.Column(db.Integer, db.ForeignKey('users.id'))
    icon_id           = db.Column(db.Integer, db.ForeignKey('icons.id'))
    activate          = db.Column(db.Boolean, default=True)

    color             = db.relationship("Color", lazy='joined')
    icon              = db.relationship("Icon", lazy='joined')

def __init__(self, description, total, end_date, color_id, icon_id, user_id, is_expense=False, activate=True):
    self.description  = description
    self.total        = total
    self.end_date     = end_date
    self.color_id     = color_id
    self.icon_id      = icon_id
    self.user_id      = user_id
    self.is_expense   = is_expense
    self.activate     = activate 

