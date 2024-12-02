libros.push(libro);
localStorage.setItem('libros', JSON.stringify(libros));
displayLibros();


function displayLibros() {
listaLibros.innerHTML = '<h3>Lista de Libros</h3>';
const libros = JSON.parse(localStorage.getItem('libros')) || [];
libros.forEach(libro => {
    const div = document.createElement('div');
    div.classList.add('libro');
    div.innerHTML = `
        <p><strong>Título:</strong> ${libro.titulo}</p>
        <p><strong>Autor:</strong> ${libro.autor}</p>
        <p><strong>ISBN:</strong> ${libro.isbn}</p>
        <p><strong>Año:</strong> ${libro.año}</p>
        <p><strong>Categoría:</strong> ${libro.categoria}</p>
        <p><strong>Estado:</strong> ${libro.estado}</p>
    `;
    listaLibros.appendChild(div);
});
updateSelectOptions('libroPrestamo', libros.filter(libro => libro.estado === 'disponible'), 'titulo');
updateSelectOptions('libroReserva', libros.filter(libro => libro.estado === 'disponible'), 'titulo');
updateSelectOptions('prestamoDevolucion', libros.filter(libro => libro.estado === 'prestado'), 'titulo');
}

function updateSelectOptions(selectId, items, key) {
const select = document.getElementById(selectId);
if (select) {
    select.innerHTML = '';
    items.forEach(item => {
        const option = document.createElement('option');
        option.value = item[key];
        option.textContent = item[key];
        select.appendChild(option);
    });
}
}

displayLibros();

