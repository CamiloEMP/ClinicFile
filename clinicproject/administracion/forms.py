from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, SelectField, StringField, PasswordField
from wtforms.fields.html5 import DateTimeLocalField, DateField, EmailField, IntegerField
from wtforms import validators

from clinicproject.models import User

class RegistroMedicoForm(FlaskForm):
    nombre = StringField('Nombres y Apellidos')
    telefono = IntegerField('Télefono de contacto')
    tipo_documento = SelectField('Tipo de documento',
                     choices=[(1, 'Cédula de ciudadanía'),
                              (2, 'Cédula extranjera'),
                              (3, 'Pasaporte'),
                              (4, 'Tarjeta de identidad'),
                              (5, 'Registro civil')])
    no_documento = IntegerField('Número de documento')
    fecha_nacimiento = DateField('Fecha de nacimiento',  format='%Y-%m-%d')
    correo = EmailField('Correo electrónico', [validators.DataRequired(), validators.Email()])
    username = StringField('Username')
    password = PasswordField('Contraseña')
    terminos = BooleanField("Declaro haber leído y aceptado la normativa sobre protección de datos.")
    enviar = SubmitField('Enviar')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise validators.ValidationError('El usuario ya existe!')

class LoginForm(FlaskForm):
    username = StringField(validators=[validators.Length(min=4, max=20)])
    password = PasswordField(validators=[validators.DataRequired()])
    enviar = SubmitField("Ingresar")