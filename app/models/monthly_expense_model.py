from app                        import db
from datetime                   import datetime
from sqlalchemy.ext.declarative import declarative_base

class MonthlyExpense(db.Model):
   __tablename__      = "monthly_expense"
   id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
   start_date        = db.Column(db.DateTime, default=datetime.utcnow)
   description       = db.Column(db.String(100))
   period            = db.Column(db.Integer)
   is_paid           = db.Column(db.Boolean, default=True) 
   received          = db.Column(db.Boolean, default=False)   
   value             = db.Column(db.Float(precision=2,asdecimal=True))
   localization      = db.Column(db.String(100), nullable=True)
   category_id       = db.Column(db.Integer, db.ForeignKey("categories.id"))
   bank_account_id   = db.Column(db.Integer, db.ForeignKey("bank_accounts.id"))
   activate          = db.Column(db.Boolean, default=True)

   category          = db.relationship("Category", lazy="joined")
   bank_account      = db.relationship("BankAccount", lazy="joined")

   def __init__(self, description, period,value, category_id, bank_account_id, is_paid=True, received=True, activate=True):
       self.description     = description  
       self.period          = period  
       self.is_paid         = is_paid 
       self.received        = received  
       self.value           = value  
       self.localization    = localization     
       self.category_id     = category_id    
       self.bank_account_id = bank_account_id  
       self.activate        = activate

 