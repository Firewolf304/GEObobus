from flaskapp.SQL.database import db
import sqlalchemy

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.UUID, nullable=False, unique=True, primary_key=True)
    login = db.Column(db.Text, nullable=False, unique=True)
    data = db.Column(db.JSON)

    def __init__(self, id, login, data):
        self.id = id
        self.login = login
        self.data = data

    def __repr__(self):
        return "<User(id='%s', login='%s', data='%s')>" % (self.id,self.login,self.data)

class Login(db.Model):
    __tablename__ = "login"
    id = db.Column("id", db.UUID, nullable=False, unique=True, primary_key=True)
    password = db.Column("password", db.VARCHAR(32), nullable=False)

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def __repr__(self):
        return "<Login(id='%s', password='%s')>" % (self.id,self.password)

class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column("id", db.Integer, nullable=False, primary_key=True)
    role = db.Column("role", db.Text, nullable=False)

    def __init__(self, id, role):
        self.id = id
        self.role = role

    def __repr__(self):
        return "<Roles(id='%s', role='%s')>" % (self.id,self.role)

class Permissions(db.Model):
    __tablename__ = "permissions"
    id = db.Column("id", db.UUID, nullable=False, unique=True, primary_key=True)
    role_id = db.Column("role_id", db.Integer, nullable=False)

    def __init__(self, id, role_id):
        self.id = id
        self.role_id = role_id

    def __repr__(self):
        return "<Permissions(id='%s', role_id='%s')>" % (self.id,self.role_id)

