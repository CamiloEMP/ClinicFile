import datetime
from clinicproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))

    def __init__(self,username,password):
        self.username = username
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password, password)

class Medico(db.Model):

    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    telefono = db.Column(db.Text)
    tipo_documento = db.Column(db.Text)
    no_documento = db.Column(db.BigInteger)
    fecha_nacimiento = db.Column(db.Date)
    correo = db.Column(db.Text)
    usuario_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    usuario = db.relationship('User' ,uselist=False)

    def __init__(self, nombre, telefono, tipo_documento, no_documento, fecha_nacimiento, correo, usuario_id):
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.no_documento = no_documento
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.usuario_id = usuario_id

class Paciente(db.Model):

    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    telefono = db.Column(db.Text)
    tipo_documento = db.Column(db.Text)
    no_documento = db.Column(db.BigInteger)
    fecha_nacimiento = db.Column(db.Date)
    correo = db.Column(db.Text)
    usuario_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    usuario = db.relationship('User' ,uselist=False)

    def __init__(self, nombre, telefono, tipo_documento, no_documento, fecha_nacimiento, correo, usuario_id):
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.no_documento = no_documento
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.usuario_id = usuario_id

class Cita(db.Model):

    __tablename__ = 'citas'

    id = db.Column(db.Integer, primary_key = True)
    medico_id = db.Column(db.Integer,db.ForeignKey('medicos.id'))
    medico = db.relationship('Medico', uselist=False)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    duracion = db.Column(db.Integer)
    estado = db.Column(db.Text)
    paciente_id = db.Column(db.Integer,db.ForeignKey('pacientes.id'))
    paciente = db.relationship('Paciente' ,uselist=False)
    comentarios = db.relationship('CitaComentario', backref="cita_comentario", lazy="dynamic")

    def __init__(self, medico_id, fecha, hora, duracion):
        self.medico_id = medico_id
        self.fecha = fecha
        self.hora = hora
        self.duracion = duracion
        self.estado = 'disponible'

class CitaComentario(db.Model):

    __tablename__ = 'citas_comentario'
    id = db.Column(db.Integer, primary_key = True)
    cita_id = db.Column(db.Integer,db.ForeignKey('citas.id'))
    fecha_hora = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comentario = db.Column(db.Text)

    def __init__(self, cita_id, commentario):
        self.cita_id = cita_id
        self.comentario = commentario

    