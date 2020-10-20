from  app.utils.oauth                 import login_required     
from  flask_restplus                  import Resource
from  app.routes                      import categories_route
from  app.services.categories_service import CategoriesService

@categories_route.route('/')
@categories_route.response(404, 'Page not found')
@categories_route.response(500, ';(')
class CategoriesController(Resource):
    @login_required
    def get(self):
        try:
            return CategoriesService.list_all(), 200
        except Exception as e:
            return {"msg": "Key error"}, 404

categories_route.add_resource(CategoriesController, '/', methods=['GET', 'POST'])
        