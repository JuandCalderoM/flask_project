function SoloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm ";
    especiales = [8, 13];
    tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}
function SoloNumeros(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "0123456789";
    especiales = [8, 13];
    tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}
function clave(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "0123456789QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm  @'()``:,.";
    especiales = [8, 13];
    tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}
function Correo(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toString();
    letras = "0123456789QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm@._-";
    especiales = [8, 13];
    tecla_especial = false;
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }
    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        return false;
    }
}
//para el caso de el login 
const pass = document.getElementById('password-field');
const icon = document.querySelector('.bx');

icon.addEventListener('click', e => {
    if (pass.type === 'password') {
        pass.type = 'text';
        icon.classList.remove('bx-show');  // Remueve la clase "mostrar"
        icon.classList.add('bx-hide');     // Agrega la clase "ocultar"
    } else {
        pass.type = 'password';
        icon.classList.remove('bx-hide');  // Remueve la clase "ocultar"
        icon.classList.add('bx-show');     // Agrega la clase "mostrar"
    }
});
