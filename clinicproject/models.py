from clinicproject import db

class Medico(db.Model):

    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)

    def __init__(self, nombre):
        self.nombre = nombre

class Paciente(db.Model):

    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Text)
    telefono = db.Column(db.Text)
    tipo_documento = db.Column(db.Text)
    no_documento = db.Column(db.BigInteger)
    fecha_nacimiento = db.Column(db.Date)
    correo = db.Column(db.Text)
    password = db.Column(db.Text)

    def __init__(self, nombre, telefono, tipo_documento, no_documento, fecha_nacimiento, correo, password):
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.no_documento = no_documento
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.password = password

class Cita(db.Model):

    __tablename__ = 'citas'

    id = db.Column(db.Integer, primary_key = True)
    medico_id = db.Column(db.Integer,db.ForeignKey('medicos.id'))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    duracion = db.Column(db.Integer)
    estado = db.Column(db.Text)
    paciente_id = db.Column(db.Integer,db.ForeignKey('pacientes.id'))

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
    comentario = db.Column(db.Text)
