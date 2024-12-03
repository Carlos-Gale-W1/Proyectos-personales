import json
from datetime import datetime, timedelta
import time
import threading

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.cargar_tareas()
        self.iniciar_recordatorios()

    def cargar_tareas(self):
        try:
            with open('tareas.json', 'r') as archivo:
                self.tareas = json.load(archivo)
        except FileNotFoundError:
            self.tareas = []

    def guardar_tareas(self):
        with open('tareas.json', 'w') as archivo:
            json.dump(self.tareas, archivo, indent=4)

    def agregar_tarea(self):
        print("\n--- Agregar Nueva Tarea ---")
        titulo = input("Título de la tarea: ")
        descripcion = input("Descripción (opcional): ")
        
        while True:
            try:
                fecha_str = input("Fecha límite (YYYY-MM-DD): ")
                fecha_limite = datetime.strptime(fecha_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Formato de fecha inválido. Use YYYY-MM-DD")
        
        prioridad_opciones = ['Baja', 'Media', 'Alta']
        print("Prioridades:")
        for i, p in enumerate(prioridad_opciones, 1):
            print(f"{i}. {p}")
        
        while True:
            try:
                prioridad_idx = int(input("Seleccione prioridad (número): ")) - 1
                prioridad = prioridad_opciones[prioridad_idx]
                break
            except (ValueError, IndexError):
                print("Selección inválida. Intente de nuevo.")

        tarea = {
            'id': len(self.tareas) + 1,
            'titulo': titulo,
            'descripcion': descripcion,
            'fecha_limite': fecha_limite.strftime("%Y-%m-%d"),
            'prioridad': prioridad,
            'completada': False
        }

        self.tareas.append(tarea)
        self.guardar_tareas()
        print("Tarea agregada exitosamente.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        print("\n--- Lista de Tareas ---")
        for tarea in self.tareas:
            estado = "✓" if tarea['completada'] else " "
            print(f"[{estado}] ID: {tarea['id']} | {tarea['titulo']} | "
                  f"Límite: {tarea['fecha_limite']} | "
                  f"Prioridad: {tarea['prioridad']}")

    def marcar_completada(self):
        self.listar_tareas()
        if not self.tareas:
            return

        try:
            id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
            for tarea in self.tareas:
                if tarea['id'] == id_tarea:
                    tarea['completada'] = True
                    self.guardar_tareas()
                    print("Tarea marcada como completada.")
                    return
            print("ID de tarea no encontrado.")
        except ValueError:
            print("ID inválido.")

    def recordatorio_tareas(self):
        while True:
            for tarea in self.tareas:
                if not tarea['completada']:
                    fecha_limite = datetime.strptime(tarea['fecha_limite'], "%Y-%m-%d")
                    dias_restantes = (fecha_limite - datetime.now()).days

                    if 0 <= dias_restantes <= 3:
                        print(f"\n🚨 RECORDATORIO: Tarea '{tarea['titulo']}' "
                              f"vence en {dias_restantes} días!")
            
            time.sleep(3600)  # Revisar cada hora

    def iniciar_recordatorios(self):
        hilo_recordatorios = threading.Thread(target=self.recordatorio_tareas, daemon=True)
        hilo_recordatorios.start()

def menu_principal():
    gestor = GestorTareas()
    
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar Nueva Tarea")
        print("2. Listar Tareas")
        print("3. Marcar Tarea como Completada")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            gestor.agregar_tarea()
        elif opcion == '2':
            gestor.listar_tareas()
        elif opcion == '3':
            gestor.marcar_completada()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
