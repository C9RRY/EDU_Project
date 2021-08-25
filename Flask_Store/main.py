import hashlib
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String)
    password = db.Column(db.String)
    salt = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    user_name = 'Гість'
    user_rights = 'quest'
    base_for_user = 'base.html'

    def __repr__(self):
        return self.user


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.String)

    def __repr__(self):
        return self.title


def encode_to_hash(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key, salt


def check_password(old_password_key, new_password, salt):
    new_password_key = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt, 100000)
    if old_password_key == new_password_key:
        pass_correct = True
    else:
        pass_correct = False
    return pass_correct


@app.route('/')
def index():
    arg = Users.base_for_user
    print(arg)
    items = Items.query.order_by(Items.price).all()
    return render_template('index.html', data=items, args=Users.base_for_user, user=Users.user_name)


@app.route('/about')
def about():
    return render_template('about.html', args=Users.base_for_user, user=Users.user_name)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        create_time = time.asctime()
        print(create_time)
        item = Items(title=title, price=price, create_time=create_time)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка поля"
    else:
        return render_template('create.html', args=Users.base_for_user, user=Users.user_name)


@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html', args=Users.base_for_user, user=Users.user_name)


@app.route('/reg_or_log')
def reg_or_log():
    Users.user_name = "Гість"
    Users.user_rights = "quest"
    Users.base_for_user = "base.html"
    return render_template('reg_or_log.html', args=Users.base_for_user)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        base_users = Users.query.all()
        for u in base_users:
            print(u)
            if str(u) == str(user):
                return render_template('/registration.html', data="Логін зайнятий")
        crypt_password, salt = encode_to_hash(password)
        users = Users(user=user, password=crypt_password, salt=salt)
        try:
            db.session.add(users)
            db.session.commit()
            Users.user_name = user
            Users.user_rights = 'user'
            Users.base_for_user = 'base_user.html'
            items = Items.query.order_by(Items.price).all()

            return render_template('index.html', data=items, args=Users.base_for_user, user=Users.user_name)
        except:
            return "Помилка поля"
    else:
        return render_template('registration.html')


@app.route('/management')
def management():
    arg = Users.base_for_user
    print(arg)
    users = Users.query.order_by(Users.user).all()
    return render_template('management.html', data=users, args=Users.base_for_user, user=Users.user_name)


@app.route('/input_user', methods=['POST', 'GET'])
def input_user():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        items = Items.query.order_by(Items.price).all()
        for usr in Users.query.all():
            print(usr)
            if str(usr) == user:
                is_logged = check_password(usr.password, password, usr.salt)
                if is_logged is True:
                    Users.user_name = usr
                    if usr.is_admin is True:
                        print(items)
                        Users.user_rights = 'admin'
                        Users.base_for_user = 'base_admin.html'
                        return render_template('index.html', data=items, args=Users.base_for_user, user=Users.user_name)
                    else:
                        Users.user_rights = 'user'
                        Users.base_for_user = 'base_user.html'
                        return render_template('index.html', data=items, args=Users.base_for_user, user=Users.user_name)
                return render_template('/input_user.html', data="Помилка пароля")
        return render_template('/input_user.html', data="Не існує")
    return render_template('input_user.html')


if __name__ == "__main__":
    app.run(debug=True)

