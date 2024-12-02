document.addEventListener('DOMContentLoaded', () => {
    const devolucionForm = document.getElementById('devolucionForm');
    const listaDevoluciones = document.getElementById('listaDevoluciones');

    devolucionForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const libro = document.getElementById('prestamoDevolucion').value;

        const devolucion = {
            libro,
            fechaDevolucion: new Date().toISOString().split('T')[0]
        };

        addDevolucion(devolucion);
        devolucionForm.reset();
    });

    function addDevolucion(devolucion) {
        let devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
        devoluciones.push(devolucion);
        localStorage.setItem('devoluciones', JSON.stringify(devoluciones));
        updateLibroEstado(devolucion.libro, 'disponible');
        displayDevoluciones();
    }

    function updateLibroEstado(titulo, estado) {
        let libros = JSON.parse(localStorage.getItem('libros')) || [];
        libros = libros.map(libro => {
            if (libro.titulo === titulo) {
                libro.estado = estado;
            }
            return libro;
        });
        localStorage.setItem('libros', JSON.stringify(libros));
    }

    function displayDevoluciones() {
        listaDevoluciones.innerHTML = '<h3>Lista de Devoluciones</h3>';
        const devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
        devoluciones.forEach(devolucion => {
            const div = document.createElement('div');
            div.classList.add('devolucion');
            div.innerHTML = `
                <p><strong>Libro:</strong> ${devolucion.libro}</p>
                <p><strong>Fecha de Devolución:</strong> ${devolucion.fechaDevolucion}</p>
            `;
            listaDevoluciones.appendChild(div);
        });
    }

    displayDevoluciones();
});
