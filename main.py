from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, session, render_template, request, redirect, url_for
from config import Config
from models import db, users
from sqlalchemy import create_engine
from sqlalchemy import text


app = Flask(__name__, static_folder="templates", static_url_path="/")
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

if not app.logger.handlers:
    app.logger.addHandler(handler)

app.logger.setLevel(logging.DEBUG)


app.secret_key = 'super_secret_key'

app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/')
def index():
    if 'login' in session:
        login = session['login']
        access_level = session['access_level']
        return f'Привет, {login}, ваш уровень допуска {access_level} <a href="/logout">Выйти</a>'
    app.logger.debug("sus")
    return 'Вы не вошли в систему <a href="/login">Войти</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    conn = engine.connect()

    if request.method == 'POST':
        SQL = "select password, access_level from users where login = '{0}';".format(request.form['login'])
        try:
            result = conn.execute(text(SQL))
            for row in result:
                password = row[0]
                access_level = row[1]
            if (password == request.form['password']):
                session.permanent = True  # Включаем постоянные сессии
                session['login'] = request.form['login']
                session['access_level'] = access_level
                return redirect(url_for('index'))
            else:
                return redirect(url_for('access_denied'))
        except:
            return redirect(url_for('access_denied'))

    return render_template('login.html')


@app.route('/access_denied', methods=['GET', 'POST'])
def access_denied():
    return render_template('access_denied.html')



# app.route('/loggin', methods=['GET', 'POST'], fucn = test.loggin)
    
"""@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True  # Включаем постоянные сессии
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Войти">
        </form>
    '''
"""
@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)