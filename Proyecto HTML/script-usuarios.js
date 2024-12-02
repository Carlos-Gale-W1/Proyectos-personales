document.addEventListener('DOMContentLoaded', () => {
    const usuariosForm = document.getElementById('usuariosForm');
    const listaUsuarios = document.getElementById('listaUsuarios');

    usuariosForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const nombre = document.getElementById('nombre').value;
        const direccion = document.getElementById('direccion').value;
        const telefono = document.getElementById('telefono').value;
        const correo = document.getElementById('correo').value;

        const usuario = {
            nombre,
            direccion,
            telefono,
            correo
        };

        registrarUsuario(usuario);
        usuariosForm.reset();
    });

    function registrarUsuario(usuario) {
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
                <p><strong>Correo:</strong> ${usuario.correo}</p>
            `;
            listaUsuarios.appendChild(div);
        });
    }

    displayUsuarios();
});
