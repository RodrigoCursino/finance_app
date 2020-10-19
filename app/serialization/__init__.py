from app                 import api
from flask_restplus      import fields


# Color
model_color = api.model('Color', {
    'id'         : fields.Integer,
    'color'      : fields.String,
})

# Icon
model_icon = api.model('Icon', {
    'id'        : fields.Integer,
    'icon'      : fields.String,
})

# Categories
model_categories = api.model('Category', {
    'id'         : fields.Integer,
    'description': fields.String,
    'icon'       : fields.Nested(model_icon),
    'color'      : fields.Nested(model_color),
})

# Login
model_login = api.model('Login',{
    'username' : fields.String(required=True),
    'password' : fields.String(required=True),
    'email'    : fields.String(required=True),
})

# User
model_user = api.model('User',{
    'id'       : fields.Integer,
    'username' : fields.String,
    'cellphone': fields.String,
    'name'     : fields.String,
    'password' : fields.String,
    'email'    : fields.String,
})
