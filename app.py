from flask.helpers import flash, url_for
from flask_login.utils import login_user
from clinicproject import app
from flask import render_template, redirect, request

from clinicproject.administracion.forms import LoginForm
from clinicproject.models import User

activeMenu = "home"

@app.route('/')
def index():
  activeMenu = "home"
  return render_template('index.html' , activeMenu = activeMenu)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Ingreso exitoso!')
            next = request.args.get('next')
            
            if next == None or not next[0]=='/':
                next = url_for('index')
            
            return redirect(next)
    return render_template('login.html', form = form)

if __name__ == '__main__':
  app.run(debug=True)