from flask import Blueprint, render_template, redirect, url_for, flash
from clinicproject.pacientes.forms import AgendarCitaForm, RegistroPacienteForm
from clinicproject.models import Cita, Medico, Paciente
from clinicproject import db

pacientes_blueprints = Blueprint('pacientes', __name__, template_folder='templates/citas')

@pacientes_blueprints.route('/citas', methods=['GET', 'POST'])
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
        paciente = Paciente(form.nombre.data,
                            form.telefono.data,
                            form.tipo_documento.data,
                            form.no_documento.data,
                            form.fecha_nacimiento.data,
                            form.correo.data,
                            form.password.data)
        db.session.add(paciente)
        db.session.commit()
        form = RegistroPacienteForm()
        flash("Usuario creado correctamente!!")
        return redirect(url_for('pacientes.registro'))
    else:
        if len(form.errors) != 0:
            flash(form.errors)
    return render_template('registro.html', activeMenu = activeMenu, form = form)


@pacientes_blueprints.route('/detallecita', methods=['GET', 'POST'])
def verdetallecita():
    activeMenu = "agendar"
    return render_template('detallescita.html', activeMenu = activeMenu)

@pacientes_blueprints.route('/solicitar/<idcita>', methods=['GET', 'POST'])
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