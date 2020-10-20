from app.models.category_model     import Category
from app.routes                    import categories_route
from app.serialization import model_categories

class CategoriesService():
    @staticmethod
    @categories_route.marshal_with(model_categories)
    def list_all():
        return list(Category.query.all())
    
    @staticmethod
    @categories_route.marshal_with(model_categories)
    def get_by_id(id):
        return Category.query.filter(Category.id == id).first()
    
    @staticmethod
    @categories_route.marshal_with(model_categories)
    def get_by_param(param, value):
        return Category.query.filter(getattr(Category, param) == value).first()