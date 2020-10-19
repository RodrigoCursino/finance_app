from app               import db, bcrypt, app

class User(db.Model):
    __tablename__ = "users"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username   = db.Column(db.String(100))
    name       = db.Column(db.String(100))
    cellphone  = db.Column(db.String(20), unique=True)
    password   = db.Column(db.String(255))
    email      = db.Column(db.String(120), unique=True)
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, username, name, cellphone, password, email, activate=True):
        self.username  = username
        self.name      = name
        self.cellphone = cellphone
        self.activate  = activate
        self.password  = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.email    = email
