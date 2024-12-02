#include <iostream>
#include <string>
#include <queue>  // Usamos queue para simular el orden de llegada de los clientes
#include <iomanip>  // Para dar formato al saldo
#include <vector>   // Para almacenar múltiples clientes

using namespace std;

class Cliente {
private:
    string nombre;
    string cedula;
    string numCuenta;
    double saldo;

public:
    Cliente(string nom, string ced, string numCta)
        : nombre(nom), cedula(ced), numCuenta(numCta), saldo(20000) {}  // El saldo se asigna automáticamente a 20000

    void mostrarCliente() const {
        cout << "Nombre: " << nombre << ", Cédula: " << cedula
             << ", Cuenta: " << numCuenta << ", Saldo: " << fixed << setprecision(2) << saldo << endl;
    }

    double getSaldo() const { return saldo; }

    string getNumCuenta() const { return numCuenta; }

    void consignar(double monto) {
        saldo += monto;
    }

    bool retirar(double monto) {
        if (monto <= saldo) {
            saldo -= monto;
            return true;
        }
        return false;  
    }

    bool transferir(double monto, Cliente &destino) {
        if (monto <= saldo) {
            saldo -= monto;
            destino.consignar(monto);
            return true;
        }
        return false;  
    }
};

Cliente ingresarCliente() {
    string nombre, cedula, numCuenta;

    cout << "Ingrese los datos del cliente:" << endl;
    cout << "Nombre: ";
    cin.ignore(); 
    getline(cin, nombre);
    cout << "Cédula: ";
    cin >> cedula;
    cout << "Número de cuenta: ";
    cin >> numCuenta;

    return Cliente(nombre, cedula, numCuenta);  
}

void mostrarMenu() {
    cout << "\n===== Menú =====\n";
    cout << "1. Ingresar cliente\n";
    cout << "2. Realizar transacción\n";
    cout << "3. Ver clientes registrados\n";
    cout << "4. Salir\n";
    cout << "Seleccione una opción: ";
}

void mostrarMenuTransacciones() {
    cout << "\n===== Tipo de Transacción =====\n";
    cout << "1. Consignación\n";
    cout << "2. Retiro\n";
    cout << "3. Transferencia\n";
    cout << "4. Consulta\n";
    cout << "Seleccione una opción: ";
}

void realizarTransaccion(vector<Cliente>& clientes) {
    if (clientes.empty()) {
        cout << "No hay clientes registrados.\n";
        return;
    }

    int transaccion;
    mostrarMenuTransacciones();
    cin >> transaccion;

    double monto;
    string numCuentaDestino;
    Cliente* clienteDestino = nullptr;

    switch (transaccion) {
        case 1: {  
            string numCuentaOrigen;
            cout << "Ingrese la cuenta de origen (de donde proviene el dinero): ";
            cin >> numCuentaOrigen;

            Cliente* clienteOrigen = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuentaOrigen) {
                    clienteOrigen = &c;
                    break;
                }
            }

            if (clienteOrigen == nullptr) {
                cout << "No se encontró una cuenta de origen con ese número. La consignación no se puede realizar.\n";
                return;
            }

            cout << "Ingrese el monto a consignar: ";
            cin >> monto;

            if (monto <= 0) {
                cout << "Monto inválido para la consignación.\n";
                return;
            }

            string numCuentaDestino;
            cout << "Ingrese la cuenta destino para la consignación: ";
            cin >> numCuentaDestino;

            clienteDestino = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuentaDestino) {
                    clienteDestino = &c;
                    break;
                }
            }

            if (clienteDestino == nullptr) {
                cout << "No se encontró una cuenta destino con ese número. La consignación no se puede realizar.\n";
            } else {
                clienteOrigen->retirar(monto);  
                clienteDestino->consignar(monto);  
                cout << "Consignación realizada con éxito.\n";
            }
            break;
        }
        case 2: {  
            string numCuenta;
            cout << "Ingrese el número de cuenta para realizar el retiro: ";
            cin >> numCuenta;

            Cliente* cliente = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuenta) {
                    cliente = &c;
                    break;
                }
            }

            if (cliente == nullptr) {
                cout << "No se encontró una cuenta con ese número. El retiro no se puede realizar.\n";
                return;
            }

            cout << "Ingrese el monto a retirar: ";
            cin >> monto;

            if (monto <= 0) {
                cout << "Monto inválido para el retiro.\n";
                return;
            }

            if (cliente->retirar(monto)) {
                cout << "Retiro realizado con éxito.\n";
            } else {
                cout << "Saldo insuficiente para realizar el retiro.\n";
            }
            break;
        }
        case 3: {  
            string numCuentaOrigen;
            cout << "Ingrese la cuenta de origen (de donde proviene el dinero): ";
            cin >> numCuentaOrigen;

           
            Cliente* clienteOrigen = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuentaOrigen) {
                    clienteOrigen = &c;
                    break;
                }
            }

            if (clienteOrigen == nullptr) {
                cout << "No se encontró una cuenta de origen con ese número. La transferencia no se puede realizar.\n";
                return;
            }

            cout << "Ingrese el monto a transferir: ";
            cin >> monto;

            if (monto <= 0) {
                cout << "Monto inválido para la transferencia.\n";
                return;
            }

            string numCuentaDestino;
            cout << "Ingrese la cuenta destino para la transferencia: ";
            cin >> numCuentaDestino;

            clienteDestino = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuentaDestino) {
                    clienteDestino = &c;
                    break;
                }
            }

            if (clienteDestino == nullptr) {
                cout << "No se encontró una cuenta destino con ese número. La transferencia no se puede realizar.\n";
            } else {
                if (clienteOrigen->transferir(monto, *clienteDestino)) {
                    cout << "Transferencia realizada con éxito.\n";
                } else {
                    cout << "Saldo insuficiente para realizar la transferencia.\n";
                }
            }
            break;
        }
        case 4: {  
            string numCuenta;
            cout << "Ingrese el número de cuenta para consultar el saldo: ";
            cin >> numCuenta;

            Cliente* cliente = nullptr;
            for (Cliente& c : clientes) {
                if (c.getNumCuenta() == numCuenta) {
                    cliente = &c;
                    break;
                }
            }

            if (cliente == nullptr) {
                cout << "No se encontró una cuenta con ese número.\n";
            } else {
                cout << "Saldo actual: " << fixed << setprecision(2) << cliente->getSaldo() << endl;
            }
            break;
        }
        default:
            cout << "Opción no válida.\n";
            break;
    }
}


int main() {
    vector<Cliente> clientes;  
    bool salir = false;

    while (!salir) {
        int opcion;
        mostrarMenu();
        cin >> opcion;

        switch (opcion) {
            case 1: {  
                Cliente nuevoCliente = ingresarCliente();
                clientes.push_back(nuevoCliente);
                cout << "Cliente ingresado correctamente. Saldo inicial: 20000.\n";
                break;
            }
            case 2: { 
                realizarTransaccion(clientes);
                break;
            }
            case 3: { 
                if (clientes.empty()) {
                    cout << "No hay clientes registrados.\n";
                } else {
                    for (const Cliente& c : clientes) {
                        c.mostrarCliente();
                    }
                }
                break;
            }
            case 4: {  
                salir = true;
                cout << "¡Gracias por usar el sistema bancario!\n";
                break;
            }
            default:
                cout << "Opción no válida.\n";
                break;
        }
    }

    return 0;
}
