const titleLogin = document.getElementById('title-login');
titleLogin.innerText = 'Iniciar sesión como Paciente';
document.getElementById('btn-paciente-login').addEventListener('click', () => {
  titleLogin.innerText = '';
  const message = `Iniciar sesión como Paciente`
  titleLogin.innerText = message;
})

document.getElementById('btn-medico-login').addEventListener('click', () => {
  titleLogin.innerText = '';
  const message = `Iniciar sesión como Médico`
  titleLogin.innerText = message;
})

document.getElementById('btn-admin-login').addEventListener('click', () => {
  titleLogin.innerText = '';
  const message = `Iniciar sesión como SuperAdmin`
  titleLogin.innerText = message;
})
