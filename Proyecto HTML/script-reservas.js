document.addEventListener('DOMContentLoaded', () => {
    const reservaForm = document.getElementById('reservaForm');
    const listaReservas = document.getElementById('listaReservas');

    reservaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const usuario = document.getElementById('usuarioReserva').value;
        const libro = document.getElementById('libroReserva').value;

        const reserva = {
            usuario,
            libro,
            fechaReserva: new Date().toISOString().split('T')[0]
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
                <p><strong>Fecha de Reserva:</strong> ${reserva.fechaReserva}</p>
            `;
            listaReservas.appendChild(div);
        });
    }

    displayReservas();
});
