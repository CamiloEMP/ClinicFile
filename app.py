from flask import Flask, render_template, request, redirect, flash
import os
import utils
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def prueba():
  return render_template('index.html')

@app.route('/login/')
def login_vista():
  return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def login_envio():
  return render_template('login.html')

@app.route('/registro/')
def registro_vista():
  return render_template('registro.html')

@app.route('/registro/', methods=['GET', 'POST'])
def registro_envio():
  try:
    error = None
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
      if not utils.isUsernameValid(fullname):
        error = "El nombre no debe contener simbolos o numeros"
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