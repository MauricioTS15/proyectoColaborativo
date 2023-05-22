var usuario = document.getElementById('id_username');
var usuarios = [];
var formato = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;

$.ajax({
    type: 'GET',
    url: '/appProyectos/get_users/',
    success: function(data) {
        console.log('ok');
        usuarios = data;
    },
    error: function (textStatus, errorMessage) { 
        $('p').append('Error: ' + errorMessage + ' ' + textStatus);
    }
})

usuario.addEventListener('keyup', function() {
    match = false;
    for (u of usuarios) {
        if (usuario.value == u) {
            match = true;
            break;
        }
    }
    if (!match) {
        usuario.style.borderColor = 'red';
    } else {
        usuario.style.borderColor = 'black';
    }
});

usuario.addEventListener('keyup', function() {
    if (formato.test(usuario.value)) {
        usuario.style.borderColor = 'red';
    } else {
        usuario.style.borderColor = 'black';
    }
});