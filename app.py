import re
from flask import Flask, render_template, request, redirect, flash
import os
import utils
app = Flask(__name__)
app.secret_key = os.urandom(24)
error = None
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login/')
def login_vista():
  return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def login_envio():
  try:
    if request.method == 'POST':

      correoPaciente = 'correopaciente@gmail.com'
      passwordPaciente = 'contraseñaPaciente'
      correoMedico = 'correomedico@gmail.com'
      passwordMedico = 'contraseñaMedico'
      correoAdmin = 'correoadmin@gmail.com'
      passwordAdmin = 'contraseñaAdmin'

      email = request.form['inputemaillogin']
      password = request.form['inputpasswordlogin']

      if not email or not password:
        error = 'Complete todos los campos'
        flash(error)
        return render_template('login.html')

      if correoPaciente != email or passwordPaciente != password:
        print('Entro al de usuario')
        error = 'Datos invalidos'
        flash(error)
        return render_template('login.html')
      if correoPaciente == email and passwordPaciente == password:
        return redirect('home_paciente')

      if correoMedico != email or passwordMedico != password:
        print('Entro al de medico')
        error = 'Datos invalidos'
        flash(error)
        return render_template('login.html')
      if correoMedico == email and passwordMedico == password:
        return redirect('home_medico')

      if correoAdmin != email or passwordAdmin != password:
        print('Entro al de admin')
        error = 'Datos invalidos'
        flash(error)
        return render_template('login.html')
      if correoAdmin == email and passwordAdmin == password:
        return redirect('home_admin')
  except:
    return render_template('login.html')

@app.route('/registro/')
def registro_vista():
  return render_template('registro.html')

@app.route('/registro/', methods=['GET', 'POST'])
def registro_envio():
  try:
    if request.method == 'POST':
      fullname = request.form['inputname']
      phone = request.form['inputnumber']
      type_document = request.form['inputdocumenttype']
      number_document = request.form['inputdocumentnumber']
      date = request.form['inputdate']
      email = request.form['inputemail']
      password = request.form['inputPassword']
      if not fullname or not phone or not type_document or not number_document or not date or not email or not password:
        print('entre')
        error = "Complete todos los campos"
        flash(error)
        return render_template('registro.html')
      if not utils.isNameValid(fullname):
        error = "El nombre no debe contener simbolos o numeros"
        flash(error)
        return render_template('registro.html')
      if not utils.isCellValid(number_document):
        error = "El número de documento solo debe contener números sin espacios"
        flash(error)
        return render_template('registro.html')  
      if not utils.isPasswordValid(password):
        error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
        flash(error)
        return render_template('registro.html')
      if not utils.isEmailValid(email):
        error = 'Correo invalido'
        flash(error)
        return render_template('registro.html')
  except:
    return render_template('registro.html')

@app.route('/login/home_paciente')
def home_paciente():
  return render_template('pagina_paciente_index.html')

@app.route('/login/home_medico')
def home_medico():
  return render_template('pagina_medico_index.html')

@app.route('/login/home_admin')
def home_admin():
  return render_template('pagina_admin_index.html')