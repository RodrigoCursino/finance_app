from app.models.monthly_income_model import MonthlyIncome
from app.routes                      import monthly_income_route
from app.serialization               import model_monthly_income

class MonthlyIncomeService():
    @staticmethod
    @monthly_income_route.marshal_with(model_monthly_income)
    def list_all():
        return list(MonthlyIncome.query.all())
    
    @staticmethod
    @monthly_income_route.marshal_with(model_monthly_income)
    def get_by_id(id):
        return MonthlyIncome.query.filter(MonthlyIncome.id == id).first()
    
    @staticmethod
    @monthly_income_route.marshal_with(model_monthly_income)
    def get_by_param(param, value):
        return MonthlyIncome.query.filter(getattr(MonthlyIncome, param) == value).first()