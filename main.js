let app = document.getElementById('typewriter');
 
let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});
 
typewriter
  .pauseFor(2500)
  .typeString('La Capital del Sol')
  .pauseFor(200)
  .deleteChars(10)
  .start();

function login() {
  var user, password

  user = document.getElementById('usuario').value;
  password = document.getElementById('contrasena').value;

  if (user=='prueba' && password=='123'){
    alert('Iniciaste sesion')  
  }else{
    alert('Datos incorrectos')
  }
}