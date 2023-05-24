var filterOn = document.getElementById('button-filter');
var filterOff = document.getElementById('button-exit');

// abre el menú de filtros al hacer click
filterOn.addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('button-filter').style.display = 'none';
    document.getElementById('filter-form').style.display = 'block';
    setCookie('filter', true, 1);
});

// cierra el menú de filtros al hacer click
filterOff.addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('filter-form').style.display = 'none';
    document.getElementById('button-filter').style.display = 'block';
    setCookie('filter', false, 1);
});

// guarda el tamaño de cada elemento en el array al cargar la ventana y recupera el modo de la cookie
document.addEventListener('DOMContentLoaded', function() {
    if (getCookie('filter') === 'true') {
        filterOn.click();
    } else {
        filterOff.click();
    }
});