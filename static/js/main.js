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