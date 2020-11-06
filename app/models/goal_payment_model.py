from app import db

class GoalPayment(db.Model):
    __tablename__     = "goal_payments"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value             = db.Column(db.Float(precision=2,asdecimal=True))
    payday            = db.Column(db.DateTime)
    bank_account_id   = db.Column(db.Integer, db.ForeignKey("bank_accounts.id"))
    activate          = db.Column(db.Boolean, default=True)
    
    bank_account      = db.relationship("BankAccount", lazy="joined")
   
def __init__(self, value, payday, bank_account_id, activate=True):
    self.value              = value
    self.payday             = payday
    self.bank_account_id    = bank_account_id
    self.activate           = activate 

