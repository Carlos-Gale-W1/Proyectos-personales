import os
import hashlib
import tkinter as tk
from tkinter import filedialog, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AnalizadorArchivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Archivos")
        self.root.geometry("800x600")

        # Variables
        self.ruta_seleccionada = tk.StringVar()
        self.archivos_duplicados = {}
        self.tipos_archivos = {}
        self.tamano_total = 0

        # Interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame de selección de directorio
        frame_selector = tk.Frame(self.root)
        frame_selector.pack(pady=10, padx=10, fill='x')

        tk.Label(frame_selector, text="Directorio:").pack(side=tk.LEFT)
        tk.Entry(frame_selector, textvariable=self.ruta_seleccionada, 
                 width=50).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_selector, text="Seleccionar", 
                  command=self.seleccionar_directorio).pack(side=tk.LEFT)

        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Pestaña de resumen
        frame_resumen = ttk.Frame(self.notebook)
        self.notebook.add(frame_resumen, text="Resumen")

        # Widgets de resumen
        self.texto_resumen = tk.Text(frame_resumen, height=15, width=90)
        self.texto_resumen.pack(padx=10, pady=10)

        # Pestaña de gráficos
        frame_graficos = ttk.Frame(self.notebook)
        self.notebook.add(frame_graficos, text="Gráficos")
        self.frame_graficos = frame_graficos

    def seleccionar_directorio(self):
        directorio = filedialog.askdirectory()
        if directorio:
            self.ruta_seleccionada.set(directorio)
            self.analizar_directorio(directorio)

    def analizar_directorio(self, directorio):
        # Reiniciar variables
        self.archivos_duplicados = {}
        self.tipos_archivos = {}
        self.tamano_total = 0
        hashes = {}

        # Analizar archivos
        for raiz, _, archivos in os.walk(directorio):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    # Información básica
                    tamano = os.path.getsize(ruta_completa)
                    self.tamano_total += tamano
                    extension = os.path.splitext(archivo)[1]

                    # Conteo de tipos de archivos
                    self.tipos_archivos[extension] = \
                        self.tipos_archivos.get(extension, 0) + 1

                    # Detectar archivos duplicados
                    with open(ruta_completa, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                        if file_hash in hashes:
                            if file_hash not in self.archivos_duplicados:
                                self.archivos_duplicados[file_hash] = [hashes[file_hash]]
                            self.archivos_duplicados[file_hash].append(ruta_completa)
                        else:
                            hashes[file_hash] = ruta_completa

                except Exception as e:
                    print(f"Error analizando {ruta_completa}: {e}")

        # Mostrar resultados
        self.mostrar_resumen()
        self.mostrar_graficos()

    def mostrar_resumen(self):
        self.texto_resumen.delete('1.0', tk.END)
        
        # Resumen de archivos
        self.texto_resumen.insert(tk.END, 
            f"Directorio Analizado: {self.ruta_seleccionada.get()}\n")
        self.texto_resumen.insert(tk.END, 
            f"Tamaño Total: {self.tamano_total / (1024*1024):.2f} MB\n\n")

        # Tipos de archivos
        self.texto_resumen.insert(tk.END, "Distribución de Tipos de Archivos:\n")
        for ext, count in sorted(self.tipos_archivos.items(), 
                                 key=lambda x: x[1], reverse=True):
            self.texto_resumen.insert(tk.END, f"{ext}: {count} archivos\n")

        # Archivos duplicados
        self.texto_resumen.insert(tk.END, "\nArchivos Duplicados:\n")
        for hash_duplicado, archivos in self.archivos_duplicados.items():
            if len(archivos) > 1:
                self.texto_resumen.insert(tk.END, 
                    f"Duplicados ({len(archivos)} copias):\n")
                for archivo in archivos:
                    self.texto_resumen.insert(tk.END, f"- {archivo}\n")

    def mostrar_graficos(self):
        # Limpiar gráficos previos
        for widget in self.frame_graficos.winfo_children():
            widget.destroy()

        # Gráfico de tipos de archivos
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Pastel de tipos de archivos
        ax1.pie(list(self.tipos_archivos.values()), 
                labels=list(self.tipos_archivos.keys()), 
                autopct='%1.1f%%')
        ax1.set_title('Distribución de Tipos de Archivos')

        # Barras de tipos de archivos
        ax2.bar(list(self.tipos_archivos.keys()), 
                list(self.tipos_archivos.values()))
        ax2.set_title('Número de Archivos por Tipo')
        plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

        plt.tight_layout()

        # Incrustar gráfico en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame_graficos)
        canvas.draw()
        canvas.get_tk_widget().pack()

def iniciar_analizador():
    root = tk.Tk()
    app = AnalizadorArchivos(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_analizador()
