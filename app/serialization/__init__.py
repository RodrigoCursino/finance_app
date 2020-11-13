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

# Bank  
model_bank = api.model('Bank', {
    'id'    : fields.Integer,
    'name'  : fields.String,
    'code'  : fields.String,
    'brand' : fields.String,
})

# Categories
model_categories = api.model('Category', {
    'id'         : fields.Integer,
    'description': fields.String,
    'icon'       : fields.Nested(model_icon),
    'color'      : fields.Nested(model_color),
})

# CreditCardBanner
model_credit_card_banner = api.model('CreditCardBanner', {
    'id'     : fields.Integer,
    'name'   : fields.String,
    'brand'  : fields.Integer,
})

# CreditCard
model_credit_card = api.model('CreditCard', {
    'description'                  : fields.String,
    'close_day'                    : fields.Integer,
    'pay_day'                      : fields.Integer,
    'budget_limit'                 : fields.Float,
    'bank_id'                      : fields.Integer,
    'credit_card_banner_id'        : fields.Integer,
    'credit_card_invoice_reminder' : fields.Boolean,
    'activate'                     : fields.Boolean,
    'bank'                         : fields.Nested(model_bank),
    'credit_card_banner'           : fields.Nested(model_credit_card_banner),
})

# Login
model_login = api.model('User',{
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

# Account Type
model_account_type = api.model('AccountType', {
    'id'   : fields.Integer,
    'name' : fields.String,
    'icon' : fields.Nested(model_icon),
})

# Bank Account 
model_bank_account = api.model('BankAccount', {
    'id'                 : fields.Integer,
    'name'               : fields.String,
    'description'        : fields.String,
    'bank'               : fields.Nested(model_bank),
    'color'              : fields.Nested(model_color),
    'account_type'       : fields.Nested(model_account_type),
    'check_in_home'      : fields.Boolean,
})

# Monthly Income
model_monthly_income = api.model('MonthlyIncome',{
    'id'           : fields.Integer,
    'start_date'   : fields.DateTime,      
    'description'  : fields.DateTime,     
    'period'       : fields.Integer,         
    'recurring'    : fields.Boolean,       
    'received'     : fields.Boolean,          
    'value'        : fields.Float,           
    'category'     : fields.Nested(model_categories),     
    'bank_account' : fields.Nested(model_bank_account),          
})
