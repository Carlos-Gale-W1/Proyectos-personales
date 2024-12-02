#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <limits>
#include <ctime>
using namespace std;
//profesora copile esto en gdb online 
class Paciente {
private:
    string nombre;
    string apellido;
    string tipoConsulta;
    string horaLlegada;
    string celular;
    string acompanante;
    string diagnostico;
    string fechaCita;
    string cedula;

public:
    Paciente(const string& nombre, const string& apellido, const string& tipo,
             const string& hora, const string& celular, const string& acompanante,
             const string& diagnostico, const string& cedula, const string& fechaCita = "")
        : nombre(nombre), apellido(apellido), tipoConsulta(tipo), horaLlegada(hora),
          celular(celular), acompanante(acompanante), diagnostico(diagnostico), 
          cedula(cedula), fechaCita(fechaCita) {}

    void mostrar() const {
        cout << "Nombre: " << nombre << " " << apellido
             << ", Tipo: " << tipoConsulta
             << ", Hora: " << horaLlegada
             << ", Celular: " << celular
             << ", Acompañante: " << acompanante
             << ", Diagnóstico: " << diagnostico;
        if (!fechaCita.empty()) {
            cout << ", Fecha Cita: " << fechaCita;
        }
        cout << ", Cédula: " << cedula << endl;
    }

    string obtenerNombre() const {
        return nombre;
    }

    string obtenerCedula() const {
        return cedula;
    }

    string obtenerTipoConsulta() const {
        return tipoConsulta;
    }
};

bool esNumero(const string& str) {
    for (char c : str) {
        if (!isdigit(c)) {
            return false;
        }
    }
    return true;
}

string generarFechaCita() {
    time_t t = time(0);
    struct tm* now = localtime(&t);
    
    char fecha[20];
    strftime(fecha, sizeof(fecha), "%d/%m/%Y", now);
    
    return string(fecha);
}

class ListaSimple {
private:
    vector<Paciente> listaPacientes;

public:
    void agregarPaciente(const Paciente& paciente) {
        listaPacientes.push_back(paciente);
    }

    void mostrarLista() {
        if (listaPacientes.empty()) {
            cout << "No hay pacientes en la lista de espera.\n";
        } else {
            for (const auto& paciente : listaPacientes) {
                paciente.mostrar();
            }
        }
    }

    Paciente* buscarPorNombre(const string& nombre) {
        for (auto& paciente : listaPacientes) {
            if (paciente.obtenerNombre() == nombre) {
                return &paciente;
            }
        }
        return nullptr;
    }

    Paciente* buscarPorCedula(const string& cedula) {
        for (auto& paciente : listaPacientes) {
            if (paciente.obtenerCedula() == cedula) {
                return &paciente;
            }
        }
        return nullptr;
    }
};

class Cola {
private:
    queue<Paciente> cola;

public:
    void agregarPaciente(const Paciente& paciente) {
        cola.push(paciente);
    }

    void atenderPaciente() {
        if (!cola.empty()) {
            cout << "Atendiendo paciente: ";
            cola.front().mostrar();
            cola.pop();
        } else {
            cout << "No hay pacientes en la cola de urgencias.\n";
        }
    }

    void mostrarPacientes() {
        if (cola.empty()) {
            cout << "No hay pacientes en la cola de urgencias.\n";
        } else {
            queue<Paciente> temp = cola;
            while (!temp.empty()) {
                temp.front().mostrar();
                temp.pop();
            }
        }
    }
};

class Pila {
private:
    stack<Paciente> pila;

public:
    void agregarPaciente(const Paciente& paciente) {
        pila.push(paciente);
    }

    void mostrarPacientes() {
        if (pila.empty()) {
            cout << "No hay pacientes atendidos.\n";
        } else {
            stack<Paciente> temp = pila;
            while (!temp.empty()) {
                temp.top().mostrar();
                temp.pop();
            }
        }
    }
};

int main() {
    ListaSimple lista;
    Cola colaUrgencias;
    Pila pilaAtendidos;

    int opcion;
    do {
        cout << "\n--- Sistema de Gestión de Atención en una Clínica ---\n";
        cout << "1. Agregar Paciente\n";
        cout << "2. Atender Paciente\n";
        cout << "3. Deshacer Atención\n";
        cout << "4. Mostrar Pacientes en Lista de Espera\n";
        cout << "5. Mostrar Pacientes Atendidos\n";
        cout << "6. Eliminar Paciente\n";
        cout << "7. Buscar Paciente\n";
        cout << "0. Salir\n";
        cout << "Ingrese una opción: ";
        cin >> opcion;

        switch (opcion) {
        case 1: {
            string nombre, apellido, tipo, hora, celular, acompanante, diagnostico, cedula, fechaCita;
            cout << "Ingrese nombre: ";
            cin >> nombre;
            cout << "Ingrese apellido: ";
            cin >> apellido;

            do {
                cout << "Ingrese tipo de consulta (Urgente/General): ";
                cin >> tipo;
                if (tipo != "Urgente" && tipo != "General") {
                    cout << "Solo puede ser 'Urgente' o 'General'. Intente nuevamente.\n";
                }
            } while (tipo != "Urgente" && tipo != "General");

            bool horaValida = false;
            do {
                cout << "Ingrese hora de llegada (ej. 10:30 AM o 10:30 PM): ";
                cin >> hora;
                if (hora.find("AM") != string::npos || hora.find("PM") != string::npos) {
                    horaValida = true;
                } else {
                    cout << "Debe ingresar la hora en formato AM o PM. Intente nuevamente.\n";
                }
            } while (!horaValida);

            cout << "Ingrese número de celular: ";
            cin >> celular;
            cout << "Ingrese nombre de acompañante: ";
            cin >> acompanante;
            cout << "Ingrese diagnóstico: ";
            cin >> diagnostico;

            bool cedulaValida = false;
            do {
                cout << "Ingrese número de cédula: ";
                cin >> cedula;
                if (!cedula.empty() && esNumero(cedula)) {
                    cedulaValida = true;
                } else {
                    cout << "La cédula debe ser un número válido. Intente nuevamente.\n";
                }
            } while (!cedulaValida);

            if (tipo == "General") {
                fechaCita = generarFechaCita();
            }

            Paciente p(nombre, apellido, tipo, hora, celular, acompanante, diagnostico, cedula, fechaCita);
            if (tipo == "Urgente") {
                colaUrgencias.agregarPaciente(p);
            } else {
                lista.agregarPaciente(p);
            }
            break;
        }
        case 2:
            colaUrgencias.atenderPaciente();
            break;
        case 3:
            cout << "Funcionalidad pendiente para deshacer atención.\n";
            break;
        case 4:
            cout << "Pacientes en Lista de Espera:\n";
            lista.mostrarLista();
            break;
        case 5:
            cout << "Pacientes Atendidos:\n";
            pilaAtendidos.mostrarPacientes();
            break;
        case 6:
            cout << "Funcionalidad pendiente para eliminar paciente.\n";
            break;
        case 7: {
            int subOpcion;
            cout << "Buscar paciente por:\n";
            cout << "1. Nombre\n";
            cout << "2. Cédula\n";
            cout << "Ingrese una opción: ";
            cin >> subOpcion;

            if (subOpcion == 1) {
                string nombre;
                cout << "Ingrese el nombre del paciente: ";
                cin >> nombre;
                Paciente* paciente = lista.buscarPorNombre(nombre);
                if (paciente) {
                    paciente->mostrar();
                } else {
                    cout << "Paciente no encontrado.\n";
                }
            } else if (subOpcion == 2) {
                string cedula;
                cout << "Ingrese la cédula del paciente: ";
                cin >> cedula;
                Paciente* paciente = lista.buscarPorCedula(cedula);
                if (paciente) {
                    paciente->mostrar();
                } else {
                    cout << "Paciente no encontrado.\n";
                }
            } else {
                cout << "Opción inválida.\n";
            }
            break;
        }
        case 0:
            cout << "Saliendo del sistema...\n";
            break;
        default:
            cout << "Opción no válida.\n";
        }
    } while (opcion != 0);

    return 0;
}


