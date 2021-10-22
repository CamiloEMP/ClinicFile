from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms import BooleanField, SubmitField, SelectField, StringField, PasswordField
from wtforms.fields.core import RadioField
from wtforms.fields.html5 import DateTimeLocalField, DateField, EmailField, IntegerField,TimeField
from wtforms import validators
from wtforms.fields.simple import HiddenField


class FiltrarCitasForm(FlaskForm):
    filtros = RadioField('Filtrar cita por:',
            choices=[('todo', 'Todo'), ('idPaciente', 'No Documento')
                    ,('paciente', 'Paciente'), ('estado', 'Estado Cita')
                    ,('FechaLabel', 'Fecha')])
    filtro = StringField('')
    fecha = DateField('Fecha',  format='%Y-%m-%d')
    selectEstados = SelectField('Seleccionar Estado', 
                choices=[(1, "Solicitadas"),
                (2, "Disponibles"),
                (3, "Canceladas"),
                (4,"Cumplidas")])

class CrearCitasForm(FlaskForm):
        cantidad = IntegerField('Cantidad de citas')
        duracion = IntegerField('Duración de citas (Minutos)')
        dia = DateField('Seleccionar Día', format='%Y-%m-%d')
        hora = TimeField('Hora Inicio', format='%H:%M')
        crear = SubmitField('Crear Cita')

class CrearComentarioForm(FlaskForm):
        comentario = StringField([validators.Length(min=10, max=250)])
        idcita = HiddenField([validators.DataRequired(), validators.Email()])
        crear = SubmitField('Añadir')