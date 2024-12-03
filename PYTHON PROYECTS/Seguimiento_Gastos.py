import json
from datetime import datetime

class GestorGastos:
    def __init__(self):
        self.gastos = []
        self.categorias = ['Comida', 'Transporte', 'Entretenimiento', 'Servicios', 'Otros']
        self.cargar_gastos()

    def cargar_gastos(self):
        try:
            with open('gastos.json', 'r') as archivo:
                self.gastos = json.load(archivo)
        except FileNotFoundError:
            self.gastos = []

    def guardar_gastos(self):
        with open('gastos.json', 'w') as archivo:
            json.dump(self.gastos, archivo, indent=4)

    def agregar_gasto(self):
        print("\n--- Agregar Nuevo Gasto ---")
        
        # Mostrar categorías
        print("Categorías:")
        for i, categoria in enumerate(self.categorias, 1):
            print(f"{i}. {categoria}")
        
        # Seleccionar categoría
        while True:
            try:
                seleccion = int(input("Seleccione una categoría (número): "))
                categoria = self.categorias[seleccion - 1]
                break
            except (ValueError, IndexError):
                print("Selección inválida. Intente de nuevo.")
        
        # Ingresar monto
        while True:
            try:
                monto = float(input("Ingrese el monto del gasto: "))
                break
            except ValueError:
                print("Monto inválido. Intente de nuevo.")
        
        # Descripción opcional
        descripcion = input("Descripción (opcional): ")
        
        # Agregar gasto
        gasto = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'categoria': categoria,
            'monto': monto,
            'descripcion': descripcion
        }
        
        self.gastos.append(gasto)
        self.guardar_gastos()
        print("Gasto agregado exitosamente.")

    def ver_gastos(self):
        if not self.gastos:
            print("No hay gastos registrados.")
            return

        print("\n--- Historial de Gastos ---")
        total_gastos = 0
        gastos_por_categoria = {}

        for gasto in self.gastos:
            print(f"Fecha: {gasto['fecha']}")
            print(f"Categoría: {gasto['categoria']}")
            print(f"Monto: ${gasto['monto']:.2f}")
            print(f"Descripción: {gasto['descripcion']}")
            print("---")
            
            total_gastos += gasto['monto']
            
            # Calcular gastos por categoría
            categoria = gasto['categoria']
            gastos_por_categoria[categoria] = gastos_por_categoria.get(categoria, 0) + gasto['monto']

        print(f"\nTotal de gastos: ${total_gastos:.2f}")
        
        print("\n--- Resumen por Categoría ---")
        for categoria, total in gastos_por_categoria.items():
            print(f"{categoria}: ${total:.2f}")

def menu_principal():
    gestor = GestorGastos()
    
    while True:
        print("\n--- Gestor de Gastos ---")
        print("1. Agregar Nuevo Gasto")
        print("2. Ver Historial de Gastos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            gestor.agregar_gasto()
        elif opcion == '2':
            gestor.ver_gastos()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()