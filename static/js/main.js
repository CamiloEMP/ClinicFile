// Animacion boton hacia arriba
window.onscroll = function() {
  if (document.documentElement.scrollTop > 80){
    document.querySelector('.contenedor-boton').classList.add('show');
  } else {
    document.querySelector('.contenedor-boton').classList.remove('show');
  }
}

document.querySelector('.contenedor-boton').addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  })
})

function paginaAtras() {
  window.location="../../templates/listadocitas.html"
}

document.querySelectorAll('.li-medico').forEach(element => {
  const btnDelt = document.createElement('button');
  const btnEdit = document.createElement('button');
  const contentbtnDelt = document.createTextNode("Eliminar");
  const contentbtnEdit = document.createTextNode("Editar");
  btnDelt.appendChild(contentbtnDelt);
  btnEdit.appendChild(contentbtnEdit);
  btnDelt.className = 'btn-delete-edit btn-delete';
  btnEdit.className = 'btn-delete-edit btn-edit';

  element.innerHTML = `${element.textContent} ${element.after(btnDelt)} ${element.after(btnEdit)}`
});