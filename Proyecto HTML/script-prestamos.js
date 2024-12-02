document.addEventListener('DOMContentLoaded', () => {
    const prestamoForm = document.getElementById('prestamoForm');
    const listaPrestamos = document.getElementById('listaPrestamos');

    prestamoForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const usuario = document.getElementById('usuarioPrestamo').value;
        const libro = document.getElementById('libroPrestamo').value;
        const fechaPrestamo = document.getElementById('fechaPrestamo').value;
        const fechaDevolucion = document.getElementById('fechaDevolucion').value;

        const prestamo = {
            usuario,
            libro,
            fechaPrestamo,
            fechaDevolucion
        };

        addPrestamo(prestamo);
        prestamoForm.reset();
    });

    function addPrestamo(prestamo) {
        let prestamos = JSON.parse(localStorage.getItem('prestamos')) || [];
        prestamos.push(prestamo);
        localStorage.setItem('prestamos', JSON.stringify(prestamos));
        updateLibroEstado(prestamo.libro, 'prestado');
        displayPrestamos();
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

    function displayPrestamos() {
        listaPrestamos.innerHTML = '<h3>Lista de Préstamos</h3>';
        const prestamos = JSON.parse(localStorage.getItem('prestamos')) || [];
        prestamos.forEach(prestamo => {
            const div = document.createElement('div');
            div.classList.add('prestamo');
            div.innerHTML = `
                <p><strong>Usuario:</strong> ${prestamo.usuario}</p>
                <p><strong>Libro:</strong> ${prestamo.libro}</p>
                <p><strong>Fecha de Préstamo:</strong> ${prestamo.fechaPrestamo}</p>
                <p><strong>Fecha de Devolución:</strong> ${prestamo.fechaDevolucion}</p>
            `;
            listaPrestamos.appendChild(div);
        });
    }

    displayPrestamos();
});
