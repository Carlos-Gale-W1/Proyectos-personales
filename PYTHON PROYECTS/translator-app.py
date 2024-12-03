import googletrans
from googletrans import Translator
import tkinter as tk
from tkinter import ttk

class TraductorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traductor Universal")
        self.root.geometry("600x400")

        self.idiomas = googletrans.LANGUAGES

        tk.Label(root, text="Texto a Traducir:").pack(pady=5)
        self.texto_entrada = tk.Text(root, height=5, width=70)
        self.texto_entrada.pack(pady=5)

        frame_idiomas = tk.Frame(root)
        frame_idiomas.pack(pady=10)

        tk.Label(frame_idiomas, text="De:").grid(row=0, column=0, padx=5)
        self.combo_origen = ttk.Combobox(frame_idiomas, 
            values=list(self.idiomas.values()), width=20)
        self.combo_origen.set("spanish")
        self.combo_origen.grid(row=0, column=1, padx=5)

        tk.Label(frame_idiomas, text="A:").grid(row=0, column=2, padx=5)
        self.combo_destino = ttk.Combobox(frame_idiomas, 
            values=list(self.idiomas.values()), width=20)
        self.combo_destino.set("english")
        self.combo_destino.grid(row=0, column=3, padx=5)

        tk.Button(root, text="Traducir", command=self.traducir).pack(pady=10)

        tk.Label(root, text="Traducción:").pack(pady=5)
        self.texto_salida = tk.Text(root, height=5, width=70)
        self.texto_salida.pack(pady=5)

    def traducir(self):
        codigo_origen = next((codigo for codigo, nombre in self.idiomas.items() 
                              if nombre == self.combo_origen.get()), None)
        codigo_destino = next((codigo for codigo, nombre in self.idiomas.items() 
                               if nombre == self.combo_destino.get()), None)

        if not codigo_origen or not codigo_destino:
            self.texto_salida.delete("1.0", tk.END)
            self.texto_salida.insert(tk.END, "Error: Selección de idioma inválida.")
            return

        traductor = Translator()

        texto = self.texto_entrada.get("1.0", tk.END).strip()
        try:
            traduccion = traductor.translate(texto, 
                src=codigo_origen, 
                dest=codigo_destino)
            
            self.texto_salida.delete("1.0", tk.END)
            self.texto_salida.insert(tk.END, traduccion.text)
        except Exception as e:
            self.texto_salida.delete("1.0", tk.END)
            self.texto_salida.insert(tk.END, f"Error: {str(e)}")

def iniciar_traductor():
    root = tk.Tk()
    app = TraductorApp(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_traductor()
