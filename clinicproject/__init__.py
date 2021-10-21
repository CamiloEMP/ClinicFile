import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'passclinicsupersecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from clinicproject.pacientes.views import pacientes_blueprints
from clinicproject.medicos.views import medico_blueprints
from clinicproject.administracion.views import administrador_blueprints

app.register_blueprint(pacientes_blueprints, url_prefix = '/pacientes')
app.register_blueprint(medico_blueprints, url_prefix = '/medicos')
app.register_blueprint(administrador_blueprints, url_prefix = '/administrador')

login_manager.init_app(app)
login_manager.login_view = 'login'