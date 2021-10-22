from clinicproject import db
from clinicproject.models import Cita, CitaComentario, Medico, Paciente, Role, User
from datetime import datetime, date, time

# CREA TODAS LAS TABLAS
# INSERTA DATOS DE PRUEBAS
'''
CitaComentario.query.delete()
Cita.query.delete()
Paciente.query.delete()
Medico.query.delete()

db.session.commit()
'''
db.create_all()

rolSuper = Role('ROLE_SUPER')
rolDoctor = Role('ROLE_DOCT')
rolPaciente = Role('ROLE_PACIENTE')

db.session.add_all([rolSuper, rolDoctor, rolPaciente])
db.session.commit()

usuarioRoot = User('administrador', 'administrador', rolSuper.id)
usuarioYul = User('yuly', 'holamundo', rolPaciente.id)

userDocHouse = User('dochouse', 'dochouse', rolDoctor.id)
userDocElver = User('docemet', 'docemet', rolDoctor.id)

db.session.add_all([usuarioYul, userDocHouse, userDocElver, usuarioRoot])
db.session.commit()

docElverBrow = Medico('Emet Brown', "727563", "CC", 32456324, date.fromisoformat('2005-11-04'), "futuro@uninorte.com", userDocElver.id)
docHouse = Medico('Doc House', "7273443", "CC", 12432324, date.fromisoformat('2005-11-04'), "house@uninorte.com", userDocHouse.id)

db.session.add_all([docElverBrow, docHouse])

db.session.commit()

yulyTa = Paciente("YulyAndre N", "727263", "CC", 32432324, date.fromisoformat('2005-11-04'), "yuly@uninorte.com", usuarioYul.id)

db.session.add(yulyTa)
db.session.commit()

cita1 = Cita(docHouse.id, date.fromisoformat('2021-11-04'), time.fromisoformat("09:30:00"), 30)
cita2 = Cita(docElverBrow.id, date.fromisoformat('2021-10-10'), time.fromisoformat("08:00:00"), 30)

cita1.paciente = yulyTa


db.session.add(cita1)
db.session.add(cita2)
db.session.commit()

commentario = CitaComentario(cita1.id, "hola, usted no tiene sintomas de covid")
cita1.estado = 'Solicitado'
db.session.add(commentario)
db.session.commit()
#db.drop_all()
#db.session.commit()