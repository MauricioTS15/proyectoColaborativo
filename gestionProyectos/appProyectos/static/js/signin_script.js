var usuario = document.getElementById('id_username');
var usuarios = [];

const formato = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

const errors = document.createElement('li');

const err_format = document.createElement('small');
errors.append(err_format);

const err_exists = document.createElement('small');
errors.append(err_exists);

errors.style.display = 'none';
usuario.parentNode.after(errors);

// obtiene el listado de nombres de usuarios
fetch('/appProyectos/get_users/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(json => {usuarios = json})
.catch(error => {console.error('Error:', error)});

// evento al deseleccionar el input de nombre de usuario
usuario.addEventListener('focusout', event => {
    err_format.innerHTML = '';
    err_exists.innerHTML = '';

    let match = ExistsValidation(event);
    let spchar = FormatValidation();

    if (match || spchar) {
        usuario.style.borderColor = 'red';
        errors.style.display = 'block';
    } else {
        usuario.style.borderColor = 'black';
        errors.style.display = 'none';
    }
});

// comprueba si el usuario existe
function ExistsValidation(event) {
    usuario = event.currentTarget;
    for (u of usuarios) {
        if (usuario.value == u) {
            err_exists.innerHTML += 'El usuario ya existe.';
            return true;
        }  
    }
    return false;
}

// comprueba si se han introducido caracteres especiales
function FormatValidation() {
    if (!formato.test(usuario.value))
        return false; 
    err_format.innerHTML += 'No se admiten caracteres especiales.';
    return true;
}