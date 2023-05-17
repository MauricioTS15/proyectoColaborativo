// Obtener referencia a los botones y los elementos con la clase "cambiar-tamaño"
var aumentarBtn = document.getElementById('aumentar');
var reducirBtn = document.getElementById('reducir');
var restaurarBtn = document.getElementById('restaurar');
var elementos = document.getElementsByClassName('cambiar-tamaño');
var tamañosOriginales = [];

aumentarBtn.addEventListener('click', function () {
    for (var i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        elementos[i].style.fontSize = (fontSize + 5) + 'px';
    }
});

reducirBtn.addEventListener('click', function () {
    for (var i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        elementos[i].style.fontSize = (fontSize - 5) + 'px';
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