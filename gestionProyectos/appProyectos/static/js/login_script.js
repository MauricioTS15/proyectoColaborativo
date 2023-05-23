var usuario = document.getElementById('id_username');
var usuarios = [];

const formato = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

const errors = document.createElement('li');
errors.style.marginBottom = '10px';

const err_format = document.createElement('span');
err_format.style.color = 'red';
err_format.style.fontSize = '10px';
errors.append(err_format);

const err_exists = document.createElement('span');
err_exists.style.color = 'red';
err_exists.style.fontSize = '10px';
errors.append(err_exists);

errors.style.display = 'none';
usuario.parentNode.after(errors);

// obtiene el listado de nombres de usuarios mediante jquery
$.ajax({
    type: 'GET',
    url: '/appProyectos/get_users/',
    success: function(data) {
        usuarios = data;
    },
    error: function (textStatus, errorMessage) { 
        console.log('Error: ' + errorMessage + ' - ' + textStatus);
    }
})

// evento al deseleccionar el input de nombre de usuario
usuario.addEventListener('focusout', function(event) {
    err_format.innerHTML = '';
    err_exists.innerHTML = '';

    let match = ExistsValidation(event);
    let spchar = FormatValidation();

    if (!match || spchar) {
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
        if (usuario.value == u)
            return true;
    }
    err_exists.innerHTML += 'El usuario no existe.';
    return false;
}

// comprueba si se han introducido caracteres especiales
function FormatValidation() {
    if (!formato.test(usuario.value))
        return false; 
    err_format.innerHTML += 'No se admiten caracteres especiales.';
    return true;
}