from app import db

class CreditCard(db.Model):
    __tablename__                = "credit_cards"
    id                           = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description                  = db.Column(db.String(100))
    close_day                    = db.Column(db.Integer)
    pay_day                      = db.Column(db.Integer)
    budget_limit                 = db.Column(db.Float(precision=2, asdecimal=True))
    bank_id                      = db.Column(db.Integer, db.ForeignKey('banks.id'))
    credit_card_banner_id        = db.Column(db.Integer, db.ForeignKey('credit_card_flags.id'))
    credit_card_invoice_reminder = db.Column(db.Boolean, default=True)
    activate                     = db.Column(db.Boolean, default=True)

    bank                    = db.relationship("Bank", lazy='joined')
    credit_card_banner      = db.relationship("CreditCardBanner", lazy='joined')

def __init__(self, description, close_day, pay_day, budget_limit, bank_id, credit_card_banner_id, credit_card_invoice_reminder=True, activate=True):
    self.description                  = description
    self.close_day                    = close_day
    self.pay_day                      = pay_day    
    self.budget_limit                 = budget_limit
    self.bank_id                      = bank_id
    self.credit_card_banner_id        = credit_card_banner_id
    self.credit_card_invoice_reminder = credit_card_invoice_reminder
    self.activate                     = activate 

