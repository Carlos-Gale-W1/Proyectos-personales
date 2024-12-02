function generarReportes() {
    const reportesGenerados = document.getElementById('reportesGenerados');
    reportesGenerados.innerHTML = '<h3>Reportes Generados</h3>';

    const libros = JSON.parse(localStorage.getItem('libros')) || [];
    const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
    const prestamos = JSON.parse(localStorage.getItem('prestamos')) || [];
    const devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
    const reservas = JSON.parse(localStorage.getItem('reservas')) || [];

    const librosPrestados = prestamos.map(p => p.libro);
    const librosDisponibles = libros.filter(libro => libro.estado === 'disponible').map(libro => libro.titulo);
    const usuariosConMultas = devoluciones.filter(devolucion => {
        const prestamo = prestamos.find(p => p.libro === devolucion.libro);
        return new Date(devolucion.fechaDevolucion) > new Date(prestamo.fechaDevolucion);
    }).map(devolucion => {
        const prestamo = prestamos.find(p => p.libro === devolucion.libro);
        return prestamo.usuario;
    });

    const reportes = `
        <p><strong>Total de Libros:</strong> ${libros.length}</p>
        <p><strong>Libros Prestados:</strong> ${librosPrestados.length}</p>
        <p><strong>Libros Disponibles:</strong> ${librosDisponibles.length}</p>
        <p><strong>Usuarios con Multas:</strong> ${usuariosConMultas.length}</p>
        <p><strong>Total de Usuarios:</strong> ${usuarios.length}</p>
    `;

    reportesGenerados.innerHTML += reportes;
}
