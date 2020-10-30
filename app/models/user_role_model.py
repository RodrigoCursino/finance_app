from app               import db, bcrypt, app

class UserRole(db.Model):
    __tablename__ = "users_roles"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"))
    role_id    = db.Column(db.Integer, db.ForeignKey('roles.id'))
    activate   = db.Column(db.Boolean, default=True)

    user       = db.relationship('User', lazy="joined")
    role       = db.relationship('Role', lazy="joined")

    def __init__(self, user_id, role_id, activate=True):
        self.user_id   = user_id
        self.role_id   = role_id
        self.activate  = activate
