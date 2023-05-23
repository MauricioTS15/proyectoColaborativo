var filterOn = document.getElementById('button-filter');
filterOn.addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('button-filter').style.display = 'none';
    document.getElementById('filter-form').style.display = 'block';
});

var filterOff = document.getElementById('button-exit');
filterOff.addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('filter-form').style.display = 'none';
    document.getElementById('button-filter').style.display = 'block';
});