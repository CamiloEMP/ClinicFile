from clinicproject import app
from flask import render_template
#import os
#import utils
#app = Flask(__name__)
#app.secret_key = os.urandom(24)
#error = None
activeMenu = "home"

@app.route('/')
def index():
  activeMenu = "home"
  return render_template('index.html' , activeMenu = activeMenu)
'''
@app.route('/login/')
def login_vista():
  return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def login_envio():
  try:
    if request.method == 'POST':
      #Emails and Passwords default
      correoPaciente = 'correopaciente@gmail.com'
      passwordPaciente = 'contraseñaPaciente'
      correoMedico = 'correoMedico@gmail.com'
      passwordMedico = 'contraseñaMedico'
      correoAdmin = 'correoAdmin@gmail.com'
      passwordAdmin = 'contraseñaAdmin'
      # Inputs
      email = request.form['inputemaillogin']
      password = request.form['inputpasswordlogin']

      if not email or not password:
        error = 'Complete todos los campos'
        flash(error)
        return render_template('login.html')

      if correoPaciente == email and passwordPaciente == password:
          return redirect('home_paciente')
      elif correoMedico == email and passwordMedico == password:
        return redirect('home_medico')
      elif correoAdmin == email and password == password:
        return redirect('home_admin')

      if correoPaciente != email or passwordPaciente != password:
        error = 'Correo o contraseña invalidos'
        flash(error)
        return render_template('login.html')
      elif correoMedico != email or  passwordMedico != password:
        error = 'Correo o contraseña invalidos'
        flash(error)
        return render_template('login.html')
      elif correoAdmin != email or passwordAdmin != password:
        error = 'Correo o contraseña invalidos'
        flash(error)
        return render_template('login.html')
  except:
    return render_template('login.html')

@app.route('/registro/')
def registro_vista():
  activeMenu = "registro"
  return render_template('registro.html', activeMenu = activeMenu)

@app.route('/registro/', methods=['GET', 'POST'])
def registro_envio():
  try:
    if request.method == 'POST':
      todoOk = True
      fullname = request.form['inputname']
      phone = request.form['inputnumber']
      type_document = request.form['inputdocumenttype']
      number_document = request.form['inputdocumentnumber']
      date = request.form['inputdate']
      email = request.form['inputemail']
      password = request.form['inputPassword']
      print(password)
      if not fullname or not phone or not type_document or not number_document or not date or not email or not password:
        error = "Complete todos los campos"
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if not utils.isNameValid(fullname):
        error = "El nombre no debe contener simbolos o numeros"
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if not utils.isCellValid(number_document):
        error = "El número de documento solo debe contener números sin espacios"
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if not utils.isPasswordValid(password):
        error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if not utils.isEmailValid(email):
        error = 'Correo invalido'
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if len(phone) > 10:
        error = 'Numero de telefono invalido, maximo 10 digitos'
        flash(error)
        todoOk = False
        return render_template('registro.html')
      if todoOk:
        return render_template('login.html')
  except:
    return render_template('registro.html')

@app.route('/perfil')
def perfil():
  return render_template('perfil.html')

@app.route('/editar_perfil')
def edit_perfil():
  return render_template('editarPerfil.html')

@app.route('/home_paciente')
def home_paciente():
  activeMenu = "home"
  return render_template('pagina_paciente_index.html', activeMenu = activeMenu)

@app.route('/agendar_cita')
def agendar_cita():
  activeMenu = "agendar"
  return render_template('agendarcita.html', activeMenu = activeMenu)

@app.route('/listado_citas')
def listado_citas():
  activeMenu = "infoCitas"
  return render_template('listadocitasPaciente.html', activeMenu = activeMenu)

@app.route('/listado_citas/detalle_cita')
def detalle_cita():
  activeMenu = "detalleCita"
  return render_template('detalles_cita_paciente.html', activeMenu = activeMenu)

@app.route('/home_medico')
def home_medico():
  activeMenu = "home"
  return render_template('pagina_medico_index.html', activeMenu = activeMenu)

@app.route('/listado_citas_medico')
def listado_citas_medico():
  activeMenu = "infoCitasMedico"
  return render_template('listadocitas.html', activeMenu = activeMenu)

@app.route('/listado_citas_medico/detalle_cita_medico')
def detalle_cita_medico():
  activeMenu = "detalleCitaMedico"
  return render_template('detalles_cita_medico.html', activeMenu = activeMenu)

@app.route('/home_admin')
def home_admin():
  activeMenu = "home"
  return render_template('pagina_admin_index.html', activeMenu = activeMenu)

@app.route('/buscar_datos')
def buscar_datos():
  activeMenu = "buscar"
  return render_template('resultado_busqueda.html', activeMenu = activeMenu)
'''
if __name__ == '__main__':
  app.run(debug=True)