from clinicproject import db
from clinicproject.models import Cita, Medico, Paciente
from datetime import datetime, date, time

# CREA TODAS LAS TABLAS

'''
Cita.query.delete()
Paciente.query.delete()
Medico.query.delete()
db.session.commit()
'''
db.create_all()

docElverBrow = Medico('Emet Brown')
docHouse = Medico('Doc House')
doctorWho = Medico("Doctor Who 2")

db.session.add_all([docElverBrow, docHouse, doctorWho])

db.session.commit()

yulyTa = Paciente("YulyAndre N", "727263", "CC", 32432324, date.fromisoformat('2005-11-04'), "yuly@uninorte.com", "click")

db.session.add(yulyTa)
db.session.commit()

cita1 = Cita(docHouse.id, date.fromisoformat('2021-11-04'), time.fromisoformat("09:30:00"), 30)
cita2 = Cita(doctorWho.id, date.fromisoformat('2021-10-10'), time.fromisoformat("08:00:00"), 30)

db.session.add(cita1)
db.session.add(cita2)
db.session.commit()

#db.drop_all()
#db.session.commit()