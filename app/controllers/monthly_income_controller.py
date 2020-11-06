from  app.utils.oauth                     import login_required     
from  flask_restplus                      import Resource
from  app.routes                          import monthly_income_route
from  app.services.monthly_income_service import MonthlyIncomeService

@monthly_income_route.route('/')
@monthly_income_route.response(404, 'Page not found')
@monthly_income_route.response(500, ';(')
class MonthlyIncomeController(Resource):
    @login_required
    def get(self):
        try:
            return MonthlyIncomeService.list_all(), 200
        except Exception as e:
            return {"msg": "Key error"}, 404

monthly_income_route.add_resource(MonthlyIncomeController, '/', methods=['GET', 'POST'])
        