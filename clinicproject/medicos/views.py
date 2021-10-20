from flask import Blueprint, render_template, redirect, url_for, flash, session
from wtforms.fields.html5 import IntegerField
from clinicproject.medicos.forms import FiltrarCitasForm, CrearCitasForm
from clinicproject.models import Cita, Medico, Paciente
from clinicproject import db
from datetime import timedelta, datetime

medico_blueprints = Blueprint('medicos', __name__, template_folder='templates/citas')

@medico_blueprints.route('/citas', methods=['GET', 'POST'])
def gestionar_citas():
    form = FiltrarCitasForm()
    activeMenu = "infoCitasMedico"
    all_citas = Cita.query.all()
    front_citas = []
    for cita in all_citas:
        front_cita = {}
        if cita.estado == 'Solicitada':
            paciente = Paciente.query.get(cita.paciente_id)
            front_cita['documento'] = paciente.tipo_documento + " " + str(paciente.no_documento)
            front_cita['nombre'] = paciente.nombre
        front_cita['estado'] = cita.estado
        front_cita['id'] = cita.id
        front_cita['fecha_hora'] = str(cita.fecha) + " " + str(cita.hora)
        front_citas.append(front_cita)
    
    return render_template('listadocitas.html', form = form, activeMenu = activeMenu, citas =front_citas)

@medico_blueprints.route('/crearcitas', methods=['GET', 'POST'])
def crear_citas():
    form = CrearCitasForm()
    activeMenu = "crear_citas"

    if form.validate_on_submit():
        no_citas = range(form.cantidad.data)
        current_duration = 0
        current_time = form.hora.data
        current_datetime = datetime.combine(form.dia.data, current_time)
        for no_cita in no_citas:
            next_datetime = current_datetime + timedelta(minutes = current_duration)
            next_time = next_datetime.time()
            cita = Cita(2,form.dia.data, next_time, form.duracion.data)
            current_duration += form.duracion.data
            db.session.add(cita)
        db.session.commit()
        flash("Citas creadas correctamente!!")
        return redirect(url_for('medicos.crear_citas'))
    else:
        if len(form.errors) != 0:
            flash(form.errors)
    return render_template('crearcitas.html', form = form, activeMenu = activeMenu)

@medico_blueprints.route('/verdetallecita/<idcita>', methods=['GET', 'POST'])
def ver_detalle_citas(idcita):
    print(idcita)
    return render_template('detalles_cita_medico.html')