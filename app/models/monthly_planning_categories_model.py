from app import db

class MonthlyPlanningCategories(db.Model):
    __tablename__        = "monthly_plans_categories"
    id                   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id          = db.Column(db.Integer, db.ForeignKey('categories.id'))
    monthly_planning_id  = db.Column(db.Integer, db.ForeignKey('monthly_plans.id'))
    expense              = db.Column(db.Float(precision=2, asdecimal=True))
    notification         = db.Column(db.Boolean, default=True)
    activate             = db.Column(db.Boolean, default=True)

    category             = db.relationship('Category', lazy="joined")
    monthly_planning     = db.relationship('MonthlyPlanning', lazy="joined")

def __init__(self, category_id, monthly_planning_id, expense, monthly_income, user_id, notification=True, activate=True):
    self.category_id          = category_id  
    self.monthly_planning_id  = monthly_planning_id    
    self.expense              = expense         
    self.monthly_income       = monthly_income  
    self.user_id              = user_id  
    self.notification         = notification     
    self.activate             = activate

