from app import api

#home route
home_route       = api.namespace('home', description='Home')

#login route
login_route    = api.namespace('login', description='User Authentication')

#register route
register_route = api.namespace('register', description='User Register')

#categories route
categories_route = api.namespace('categories', description='List all categories')

#colors route
colors_route = api.namespace('colors', description='List all colors')

#icons route
icons_route = api.namespace('icons', description='List all icons')