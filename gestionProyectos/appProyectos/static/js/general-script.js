// Obtener referencia a los botones y los elementos con la clase "cambiar-tamaño"
var aumentarBtn = document.getElementById('aumentar');
var reducirBtn = document.getElementById('reducir');
var restaurarBtn = document.getElementById('restaurar');
var elementos = document.querySelectorAll('div > span');
var tamañosOriginales = [];

aumentarBtn.addEventListener('click', function () {
    for (var i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        if (fontSize < 25)
            elementos[i].style.fontSize = (fontSize + 3) + 'px';
    }
});

reducirBtn.addEventListener('click', function () {
    for (var i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        if (fontSize > 15)
            elementos[i].style.fontSize = (fontSize - 3) + 'px';
    }
});

restaurarBtn.addEventListener('click', function () {
    for (var i = 0; i < elementos.length; i++) {
        elementos[i].style.fontSize = tamañosOriginales[i];
    }
});

// IMPORTANTE PARA EL RESTAURAR: Guarda el tamaño en el array para luego poder volver a su tamaño cuando le demos al boton
document.addEventListener('DOMContentLoaded', function () {
    for (var i = 0; i < elementos.length; i++) {
        tamañosOriginales.push(window.getComputedStyle(elementos[i]).fontSize);
    }
});


// TOGGLE DARK MODE
let toggler = document.getElementById('toggle-darkmode');
toggler.addEventListener('change', function toggleDarkMode() {
    var element = document.body;
    if (this.checked) {
        element.classList.toggle("darkmode");
    } else {
        element.classList.toggle("darkmode");
    }
});