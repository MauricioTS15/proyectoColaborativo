var pwd1 = document.getElementById('id_password1');
var pwd2 = document.getElementById('id_password2');
if (pwd1 == null || pwd2 == null) {
    pwd1 = document.getElementById('id_new_password1');
    pwd2 = document.getElementById('id_new_password2');
}

const error = document.createElement('li');

const err_pwd = document.createElement('small');
error.append(err_pwd);

error.style.display = 'none';
pwd2.parentNode.after(error);

// evento al deseleccionar el input de cualquier contraseña
pwd1.addEventListener('focusout', PasswordMatch);
pwd2.addEventListener('focusout', PasswordMatch);

// comprueba si las contraseñas coinciden
function PasswordMatch() {
    err_pwd.innerHTML = '';
    if (pwd1.value != pwd2.value) {
        pwd1.style.borderColor = 'red';
        pwd2.style.borderColor = 'red';
        err_pwd.innerHTML += 'Las contraseñas no coinciden.';
        error.style.display = 'block';
    } else {
        pwd1.style.borderColor = 'black';
        pwd2.style.borderColor = 'black';
        error.style.display = 'none';
    }
}