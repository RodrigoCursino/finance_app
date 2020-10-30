from app import db

class MonthlyPlanning(db.Model):
    __tablename__     = "monthly_plans"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date        = db.Column(db.DateTime)
    percent_economy   = db.Column(db.Float(precision=2,asdecimal=False))
    monthly_income    = db.Column(db.Float(precision=2,asdecimal=True))
    user_id           = db.Column(db.Integer, db.ForeignKey("users.id"))
    activate          = db.Column(db.Boolean, default=True)

    user              = db.relationship('User', lazy="joined")

def __init__(self, start_date, percent_economy, monthly_income, user_id, activate=True):
    self.start_date      = start_date   
    self.percent_economy = percent_economy 
    self.monthly_income  = monthly_income  
    self.user_id         = user_id       
    self.activate        = activate

