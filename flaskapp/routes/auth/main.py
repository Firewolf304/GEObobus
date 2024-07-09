from flask import Blueprint, jsonify
from flaskapp.SQL.database import db
import flaskapp.SQL.models
from flaskapp.SQL.models import users

from sqlalchemy import text

authBlue = Blueprint('auth', __name__)

@authBlue.route('/')
def index():
    result = users.Users.query.all()
    data = [{'id': row.id, 'login': row.login} for row in result]
    #result = db.session.execute(text("select * from users"))
    #rows = result.fetchall()
    #data = [{'id': row.id, 'login': row.login} for row in rows]

    return str(data)

def get_blueprint():
    return authBlue