document.getElementById("formulario").addEventListener("submit", function(event){
    let hasError = false;
    let texto = document.getElementById('comentario_txt').value;

    if( texto == null || texto.length === 0) {
      alert('Error, rellena el campo comentario');
      hasError = true;
    }

    // obtenemos todos los input radio del grupo horario que estén chequeados
    // si no hay ninguno lanzamos alerta
    if(!document.querySelector('input[name="flexRadio"]:checked')) {
      alert('Error, Elige una opción de clasificación');
      hasError = true;
      }

    // si hay algún error no efectuamos la acción submit del form
    if(hasError) event.preventDefault();
});