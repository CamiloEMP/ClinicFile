from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login.utils import login_required
from flask_login import current_user
from clinicproject.pacientes.forms import AgendarCitaForm, RegistroPacienteForm
from clinicproject.models import Cita, Medico, Paciente, User
from clinicproject import db

pacientes_blueprints = Blueprint('pacientes', __name__, template_folder='templates/citas')

@pacientes_blueprints.route('/citas', methods=['GET', 'POST'])
@login_required
def agendar_cita():
    form = AgendarCitaForm()
    activeMenu = "agendar"
    all_medics = Medico.query.all()
    medicos_nombres = [(medico.id, medico.nombre) for medico in all_medics]
    form.selectNombreMedico.choices = medicos_nombres
    if form.validate_on_submit():
        #db.citas.filter(and_(db.))
        citas = db.session.query(Cita).filter(
            Cita.medico_id == form.selectNombreMedico.data,
            Cita.fecha == form.fechaCita.data
        )
        #citas = Cita.query.filter_by(fecha=form.fechaCita.data)
        return render_template('agendarcita.html', form=form, activeMenu = activeMenu, citas = citas)
    else:
        if len(form.errors) != 0:
            flash(form.errors)
    return render_template('agendarcita.html', form=form, activeMenu = activeMenu)

@pacientes_blueprints.route('/registro', methods=['GET', 'POST'])
def registro():
    activeMenu = "registro"
    form = RegistroPacienteForm()
    if form.validate_on_submit():
        form.check_username(form.username)
        usuario = User(form.username.data, form.password.data)
        db.session.add(usuario)
        db.session.commit()
        paciente = Paciente(form.nombre.data,
                            form.telefono.data,
                            form.tipo_documento.data,
                            form.no_documento.data,
                            form.fecha_nacimiento.data,
                            form.correo.data,
                            usuario.id)
        db.session.add(paciente)
        db.session.commit()
        form = RegistroPacienteForm()
        flash("Usuario creado correctamente!!")
        return redirect(url_for('pacientes.registro'))
    else:
        if len(form.errors) != 0:
            flash(form.errors)
    return render_template('registro.html', activeMenu = activeMenu, form = form)

@login_required
@pacientes_blueprints.route('/detallecita/<idcita>', methods=['GET', 'POST'])
def verdetallecita(idcita):
    activeMenu = "agendar"
    cita = Cita.query.get(idcita)
    return render_template('detallescita.html', activeMenu = activeMenu, cita = cita)


@pacientes_blueprints.route('/solicitar/<idcita>', methods=['GET', 'POST'])
@login_required
def solicitar(idcita):
    activeMenu = "agendar"
    form = AgendarCitaForm()
    all_medics = Medico.query.all()
    medicos_nombres = [(medico.id, medico.nombre) for medico in all_medics]
    form.selectNombreMedico.choices = medicos_nombres
    cita = Cita.query.get(idcita)
    cita.estado = 'Solicitada'
    cita.paciente_id = 1
    db.session.add(cita)
    db.session.commit()
    flash("Cita agendada correctamente!!")
    return redirect(url_for('pacientes.agendar_cita'))

@pacientes_blueprints.route('/miscitas', methods=['GET', 'POST'])
@login_required
def mis_citas():
    citas = Cita.query.filter_by(paciente_id = current_user.get_id())
    return render_template('miscitas.html', citas = citas)