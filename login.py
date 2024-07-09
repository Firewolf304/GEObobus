"""
from flask import Flask, session, redirect, url_for, request, render_template
from models import db, users


app = Flask(__name__, static_folder="templates", static_url_path="/")
app.logger.debug("lol")


@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.debug("lol")
    if request.method == 'POST':
        class Config:
            SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'
            SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQL = "select password from users where login = {0}".format(request.form['login'])
        #result = db.engine.execute(SQL)
        result = []
        result[0] = 1
        if (result[0] == request.form['password'] or result[0]):
            session.permanent = True  # Включаем постоянные сессии
            session['login'] = request.form['login']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('access_denied'))
    return render_template('login.html')

@app.route('/access_denied', methods=['GET', 'POST'])
def access_denied():
    return render_template('access_denied.html')

@app.route('/')
def index():
    return render_template('index.html')



"""