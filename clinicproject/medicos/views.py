from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login.utils import login_required
from wtforms.fields.html5 import IntegerField
from clinicproject.medicos.forms import FiltrarCitasForm, CrearCitasForm, CrearComentarioForm
from clinicproject.models import Cita, CitaComentario, Medico, Paciente
from clinicproject import db
from datetime import timedelta, datetime

medico_blueprints = Blueprint('medicos', __name__, template_folder='templates/citas')

@medico_blueprints.route('/citas', methods=['GET', 'POST'])
@login_required
def gestionar_citas():
    form = FiltrarCitasForm()
    activeMenu = "infoCitasMedico"
    all_citas = Cita.query.all()
    print(all_citas)
    return render_template('listadocitas.html', form = form, activeMenu = activeMenu, citas = all_citas)

@medico_blueprints.route('/crearcitas', methods=['GET', 'POST'])
@login_required
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
@login_required
def ver_detalle_citas(idcita):
    
    form = CrearComentarioForm()
    cita = Cita.query.get(idcita)
    print(cita)
    print(form)
    if form.validate_on_submit():
        citaComentario = CitaComentario(cita.id, form.comentario.data)
        cita.estado = 'Cumplida'
        db.session.add(cita)
        db.session.add(citaComentario)
        db.session.commit()

        return redirect(url_for('medicos.ver_detalle_citas', idcita = cita.id, form = form))
    if len(form.errors) != 0:
            flash(form.errors)
    return render_template('detalles_cita_medico.html', cita = cita, form = form)