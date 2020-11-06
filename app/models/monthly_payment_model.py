from   app import db
import enum

class PaymentType(enum.Enum):
    INCOME      = "INCOME"
    EXPENSE     = "EXPENSE"
    CREDIT_CARD = "CREDIT CARD"

class MonthlyPayment(db.Model):
    __tablename__     = "monthly_payments"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value             = db.Column(db.Float(precision=2,asdecimal=True))
    payday            = db.Column(db.DateTime)
    payment_type      = db.Column(db.Enum(PaymentType))
    bank_account_id   = db.Column(db.Integer, db.ForeignKey("bank_accounts.id"))
    activate          = db.Column(db.Boolean, default=True)
    
    bank_account      = db.relationship("BankAccount", lazy="joined")
   
def __init__(self, value, payday, payment_type, bank_account_id, activate=True):
    self.value              = value
    self.payday             = payday
    self.payment_type       = payment_type
    self.bank_account_id    = bank_account_id
    self.activate           = activate 

