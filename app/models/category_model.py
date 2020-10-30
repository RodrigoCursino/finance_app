from app import db

class Category(db.Model):
    __tablename__     = "categories"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description       = db.Column(db.String(100))
    is_expense        = db.Column(db.Boolean, default=False)
    user_id           = db.Column(db.Integer, db.ForeignKey('users.id'))
    color_id          = db.Column(db.Integer, db.ForeignKey('colors.id'))
    icon_id           = db.Column(db.Integer, db.ForeignKey('icons.id'))
    activate          = db.Column(db.Boolean, default=True)

    color             = db.relationship("Color", lazy='joined')
    icon              = db.relationship("Icon", lazy='joined')

def __init__(self, description, color_id, icon_id, user_id, is_expense=False, activate=True):
    self.description  = description
    self.color_id     = color_id
    self.icon_id      = icon_id
    self.user_id      = user_id
    self.is_expense   = is_expense
    self.activate     = activate 

