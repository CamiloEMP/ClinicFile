from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login.utils import login_required, login_user, logout_user
from werkzeug.wrappers import request
from clinicproject.administracion.forms import LoginForm, RegistroMedicoForm
from clinicproject.models import Cita, Medico, Paciente, Role, User
from clinicproject import db

administrador_blueprints = Blueprint('administracion', __name__, template_folder='templates/')

@administrador_blueprints.route('/registromedicos', methods=['GET', 'POST'])
@login_required
def registro():
    activeMenu = "registromedicos"
    form = RegistroMedicoForm()
    if form.validate_on_submit():
        form.check_username(form.username)
        role = Role.query.filter_by(nombre='ROLE_PACIENTE').first()
        usuario = User(form.username.data, form.password.data, role.id)
        db.session.add(usuario)
        db.session.commit()
        medico = Medico(form.nombre.data,
                            form.telefono.data,
                            form.tipo_documento.data,
                            form.no_documento.data,
                            form.fecha_nacimiento.data,
                            form.correo.data,
                            usuario.id)
        db.session.add(medico)
        db.session.commit()
        form = RegistroMedicoForm()
        flash("Usuario creado correctamente!!")
        return redirect(url_for('administracion.registro'))
    else:
        if len(form.errors) != 0:
            flash(form.errors)
    return render_template('registro_medico.html', activeMenu = activeMenu, form = form)

@administrador_blueprints.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    return render_template('perfil.html')

@administrador_blueprints.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Te has salido del sitio")
    return redirect(url_for('login'))