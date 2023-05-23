var toggler = document.getElementById('toggle-darkmode');
var aumentarBtn = document.getElementById('aumentar');
var reducirBtn = document.getElementById('reducir');
var restaurarBtn = document.getElementById('restaurar');
var elementos = document.querySelectorAll('div > span');
var tamañosOriginales = [];

toggler.addEventListener('change', toggleDarkMode);

// activa o desactiva los estilos del modo oscuro y lo guarda en una cookie
function toggleDarkMode() {
    var element = document.body;
    element.classList.toggle('darkmode');
    setCookie('darkmode', toggler.checked, 1)
}

// guarda una cookie
function setCookie(cName, cValue, expDays) {
    let date = new Date();
    date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = cName + "=" + cValue + "; " + expires + "; path=/appProyectos";
    console.log(document.cookie);
}

// recupera la cookie guardada
function getCookie(cName) {
    const name = cName + "=";
    const cDecoded = decodeURIComponent(document.cookie);
    const cArr = cDecoded .split('; ');
    let res;
    cArr.forEach(val => {
        if (val.indexOf(name) === 0) res = val.substring(name.length);
    })
    return res;
}

// guarda el tamaño de cada elemento en el array al cargar la ventana y recupera el modo de la cookie
document.addEventListener('DOMContentLoaded', function () {
    for (let i = 0; i < elementos.length; i++) {
        tamañosOriginales.push(parseFloat(window.getComputedStyle(elementos[i]).fontSize));
    }
    if (getCookie('darkmode') === 'true') {
        toggler.checked = true;
        toggleDarkMode();
    }
    console.log(document.cookie);
    console.log(getCookie('darkmode'));
});

// aumenta el tamaño de cada elemento al hacer click
aumentarBtn.addEventListener('click', function () {
    for (let i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        if (fontSize < tamañosOriginales[i]+6)
            elementos[i].style.fontSize = (fontSize + 3) + 'px';
    }
});

// reduce el tamaño de cada elemento al hacer click
reducirBtn.addEventListener('click', function () {
    for (let i = 0; i < elementos.length; i++) {
        var fontSize = parseFloat(window.getComputedStyle(elementos[i]).fontSize);
        if (fontSize > tamañosOriginales[i]-6)
            elementos[i].style.fontSize = (fontSize - 3) + 'px';
    }
});

// aplica el tamaño de cada elemento guardado en el array al hacer click
restaurarBtn.addEventListener('click', function () {
    for (let i = 0; i < elementos.length; i++) {
        elementos[i].style.fontSize = tamañosOriginales[i] + 'px';
    }
});