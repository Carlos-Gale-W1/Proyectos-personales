document.addEventListener('DOMContentLoaded', function() {
    showSection('usuarios');

    const usuarioForm = document.getElementById('usuarioForm');
    const listaUsuarios = document.getElementById('listaUsuarios');

    usuarioForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const nombre = document.getElementById('nombre').value;
        const direccion = document.getElementById('direccion').value;
        const telefono = document.getElementById('telefono').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        const usuario = {
            nombre,
            direccion,
            telefono,
            email,
            password
        };

        addUser(usuario);
        usuarioForm.reset();
    });

    function addUser(usuario) {
        let usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
        usuarios.push(usuario);
        localStorage.setItem('usuarios', JSON.stringify(usuarios));
        displayUsuarios();
    }

    function displayUsuarios() {
        listaUsuarios.innerHTML = '<h3>Lista de Usuarios</h3>';
        const usuarios = JSON.parse(localStorage.getItem('usuarios')) || [];
        usuarios.forEach(usuario => {
            const div = document.createElement('div');
            div.classList.add('usuario');
            div.innerHTML = `
                <p><strong>Nombre:</strong> ${usuario.nombre}</p>
                <p><strong>Dirección:</strong> ${usuario.direccion}</p>
                <p><strong>Teléfono:</strong> ${usuario.telefono}</p>
                <p><strong>Email:</strong> ${usuario.email}</p>
            `;
            listaUsuarios.appendChild(div);
        });
        updateSelectOptions('usuarioPrestamo', usuarios, 'nombre');
        updateSelectOptions('usuarioReserva', usuarios, 'nombre');
    }

    const libroForm = document.getElementById('libroForm');
    const listaLibros = document.getElementById('listaLibros');

    libroForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const titulo = document.getElementById('titulo').value;
        const autor = document.getElementById('autor').value;
        const isbn = document.getElementById('isbn').value;
        const año = document.getElementById('año').value;
        const categoria = document.getElementById('categoria').value;

        const libro = {
            titulo,
            autor,
            isbn,
            año,
            categoria,
            estado: 'disponible'
        };

        addBook(libro);
        libroForm.reset();
    });

    function addBook(libro) {
        let libros = JSON.parse(localStorage.getItem('libros')) || [];
        libros.push(libro);
        localStorage.setItem('libros', JSON.stringify(libros));
        displayLibros();
    }

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
        updateSelectOptions('libroPrestamo', libros, 'titulo', 'disponible');
        updateSelectOptions('libroReserva', libros, 'titulo', 'prestado');
    }

    // Préstamos de libros
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
        updateBookStatus(prestamo.libro, 'prestado');
        displayPrestamos();
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
        updateSelectOptions('prestamoDevolucion', prestamos, 'libro');
    }

    // Devoluciones de libros
    const devolucionForm = document.getElementById('devolucionForm');
    const listaDevoluciones = document.getElementById('listaDevoluciones');

    devolucionForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const libro = document.getElementById('prestamoDevolucion').value;

        const devolucion = {
            libro,
            fecha: new Date().toISOString().split('T')[0]
        };

        addDevolucion(devolucion);
        devolucionForm.reset();
    });

    function addDevolucion(devolucion) {
        let devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
        devoluciones.push(devolucion);
        localStorage.setItem('devoluciones', JSON.stringify(devoluciones));
        updateBookStatus(devolucion.libro, 'disponible');
        displayDevoluciones();
    }

    function displayDevoluciones() {
        listaDevoluciones.innerHTML = '<h3>Lista de Devoluciones</h3>';
        const devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
        devoluciones.forEach(devolucion => {
            const div = document.createElement('div');
            div.classList.add('devolucion');
            div.innerHTML = `
                <p><strong>Libro:</strong> ${devolucion.libro}</p>
                <p><strong>Fecha de Devolución:</strong> ${devolucion.fecha}</p>
            `;
            listaDevoluciones.appendChild(div);
        });
    }

    // Reservas de libros
    const reservaForm = document.getElementById('reservaForm');
    const listaReservas = document.getElementById('listaReservas');

    reservaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const usuario = document.getElementById('usuarioReserva').value;
        const libro = document.getElementById('libroReserva').value;

        const reserva = {
            usuario,
            libro,
            fecha: new Date().toISOString().split('T')[0]
        };

        addReserva(reserva);
        reservaForm.reset();
    });

    function addReserva(reserva) {
        let reservas = JSON.parse(localStorage.getItem('reservas')) || [];
        reservas.push(reserva);
        localStorage.setItem('reservas', JSON.stringify(reservas));
        displayReservas();
    }

    function displayReservas() {
        listaReservas.innerHTML = '<h3>Lista de Reservas</h3>';
        const reservas = JSON.parse(localStorage.getItem('reservas')) || [];
        reservas.forEach(reserva => {
            const div = document.createElement('div');
            div.classList.add('reserva');
            div.innerHTML = `
                <p><strong>Usuario:</strong> ${reserva.usuario}</p>
                <p><strong>Libro:</strong> ${reserva.libro}</p>
                <p><strong>Fecha de Reserva:</strong> ${reserva.fecha}</p>
            `;
            listaReservas.appendChild(div);
        });
    }

    // Generar reportes
    function generarReportes() {
        const reportesGenerados = document.getElementById('reportesGenerados');
        reportesGenerados.innerHTML = '';

        const prestamos = JSON.parse(localStorage.getItem('prestamos')) || [];
        const devoluciones = JSON.parse(localStorage.getItem('devoluciones')) || [];
        const reservas = JSON.parse(localStorage.getItem('reservas')) || [];

        const prestamosReport = `
            <h3>Reportes de Préstamos</h3>
            <p>Total de Préstamos: ${prestamos.length}</p>
        `;
        reportesGenerados.innerHTML += prestamosReport;

        const devolucionesReport = `
            <h3>Reportes de Devoluciones</h3>
            <p>Total de Devoluciones: ${devoluciones.length}</p>
        `;
        reportesGenerados.innerHTML += devolucionesReport;

        const reservasReport = `
            <h3>Reportes de Reservas</h3>
            <p>Total de Reservas: ${reservas.length}</p>
        `;
        reportesGenerados.innerHTML += reservasReport;
    }

    // Función para mostrar secciones
    function showSection(sectionId) {
        const sections = document.querySelectorAll('.section');
        sections.forEach(section => {
            section.classList.remove('active');
        });
        const section = document.getElementById(sectionId);
        if (section) {
            section.classList.add('active');
        }
    }

    // Función para actualizar opciones de selección
    function updateSelectOptions(selectId, items, key, estadoFilter = null) {
        const select = document.getElementById(selectId);
        select.innerHTML = '';
        items.forEach(item => {
            if (estadoFilter === null || item.estado === estadoFilter) {
                const option = document.createElement('option');
                option.value = item[key];
                option.textContent = item[key];
                select.appendChild(option);
            }
        });
    }

    // Inicializar la visualización de datos
    displayUsuarios();
    displayLibros();
    displayPrestamos();
    displayDevoluciones();
    displayReservas();
});
