from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    access_level = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<users {self.name}>'
