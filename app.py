# coding: utf-8

from flask import Flask
from flask import render_template, url_for, redirect
from flask import request, session

from static_inspection import static_inspection, readreport
from manage import config_checksa

from form import LoginForm, RegisterForm
from login import User
from flask_wtf.csrf import CSRFProtect
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user

app = Flask(__name__)  # type: Flask


@app.route('/')
def index():
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        if User.get(user_id):
            session['user_name'] = User.get(user_id).username
    return render_template('homepage.html', username=session['user_name'])

@app.route('/test/', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        codepath = request.form['codepath']
        static_inspection(codepath)
        report = readreport()
        return render_template('test.html', report = report)
    return render_template('test.html', username=session['user_name'])

# 登入登出
# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# csrf protection
csrf = CSRFProtect()
csrf.init_app(app)

# 登入
@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User(user_name)
        if user.verify_password(password):
            login_user(user)
            session['project'] = user.get_project()
            return redirect(request.args.get('next') or url_for('manage'))
    return render_template('login.html', title="Sign In", form=form)

# 登出
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    session['user_name'] = None
    return redirect(url_for('login'))

# 用户注册
@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name = form.username.data
            password = form.password.data
            project = form.project.data
            user = User(user_name)
            user.register(password, project)
        return render_template('login.html', title="Sign In", form=form, 
            username=session['user_name'])
    return render_template('register.html', title="Register", form=form, 
        username=session['user_name'])

@app.route('/manage/', methods=['POST','GET'])
def manage():
    if 'user_id' in session:
        user_id = session['user_id']
        if User.get(user_id):
            session['user_name'] = User.get(user_id).username
    if request.method == 'POST':
        modulenames = []
        try:
            if request.form['moudle1']:
                modulenames.append(request.form['moudle1'])
        except:
            pass
        try:
            if request.form['moudle2']:
                modulenames.append(request.form['moudle2'])
        except:
            pass
        try:
            if request.form['moudle3']:
                modulenames.append(request.form['moudle3'])
        except:
            pass
        username = session['user_name']
        print(modulenames)
        config_checksa(modulenames)
    return render_template('manage.html', username=session['user_name'])

app.secret_key = 'zxcvbnm,./'

if __name__ == '__main__':
    app.debug = True
    app.run()
