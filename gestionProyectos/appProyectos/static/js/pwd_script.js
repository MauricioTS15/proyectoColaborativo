var pwd1 = document.getElementById('id_password1');
var pwd2 = document.getElementById('id_password2');

const error = document.createElement('li');
error.style.marginBottom = '10px';
error.style.color = 'red';
error.style.fontSize = '10px';
error.style.display = 'none';
pwd2.parentNode.after(error);

// evento al deseleccionar el input de cualquier contraseña
pwd1.addEventListener('focusout', PasswordMatch);
pwd2.addEventListener('focusout', PasswordMatch);

// comprueba si las contraseñas coinciden
function PasswordMatch() {
    error.innerHTML = '';
    if (pwd1.value != pwd2.value) {
        pwd1.style.borderColor = 'red';
        pwd2.style.borderColor = 'red';
        error.innerHTML += 'Las contraseñas no coinciden.';
        error.style.display = 'block';
    } else {
        pwd1.style.borderColor = 'black';
        pwd2.style.borderColor = 'black';
        error.style.display = 'none';
    }
}