from app import db

class BankAccount(db.Model):
    __tablename__     = "bank_accounts"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name              = db.Column(db.String(150))
    description       = db.Column(db.String(850))
    bank_id           = db.Column(db.Integer, db.ForeignKey('banks.id'))
    color_id          = db.Column(db.Integer, db.ForeignKey('colors.id'))
    account_type_id   = db.Column(db.Integer, db.ForeignKey('account_types.id'))
    check_in_home     = db.Column(db.Boolean, default=False)
    activate          = db.Column(db.Boolean, default=True)

    bank              = db.relationship('Bank', lazy='joined')
    color             = db.relationship("Color", lazy='joined')
    account_type      = db.relationship('AccountType', lazy='joined')

def __init__(self, name, description, bank_id, color_id, account_type_id, check_in_home=False, activate=True):
    self.name             = name  
    self.description      = description         
    self.bank_id          = bank_id 
    self.color_id         = color_id       
    self.account_type_id  = account_type_id
    self.check_in_home    = check_in_home
    self.activate         = activate        

