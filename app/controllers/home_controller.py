from flask_restplus                import Resource
from app.routes                    import home_route

@home_route.route('/')
@home_route.response(404, 'Page not found')
@home_route.response(500, ';(')
class HomeController(Resource):
    def get(self):
        return {"Hello World": "Hello World"}