import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, messagebox

class RecomendadorPeliculas:
    def __init__(self):
        # Cargar datos (datos de ejemplo - puedes reemplazar con un dataset real)
        self.peliculas = pd.DataFrame({
            'titulo': [
                'Inception', 'Matrix', 'Interstellar', 
                'Star Wars', 'El Señor de los Anillos', 
                'Avengers', 'Batman Begins', 'Interestelar'
            ],
            'genero': [
                'Ciencia Ficción', 'Ciencia Ficción', 'Ciencia Ficción', 
                'Ciencia Ficción', 'Fantasía', 'Acción', 
                'Acción', 'Ciencia Ficción'
            ],
            'director': [
                'Christopher Nolan', 'Hnos. Wachowski', 'Christopher Nolan',
                'George Lucas', 'Peter Jackson', 'Joss Whedon', 
                'Christopher Nolan', 'Christopher Nolan'
            ],
            'descripcion': [
                'Sueños dentro de sueños', 'Realidad virtual', 
                'Viaje espacial', 'Guerra de galaxias', 
                'Aventura de fantasía', 'Superhéroes unidos', 
                'Origen de Batman', 'Viaje interestelar'
            ]
        })

        # Preparar datos para recomendación
        self.peliculas['info_combinada'] = (
            self.peliculas['titulo'] + ' ' + 
            self.peliculas['genero'] + ' ' + 
            self.peliculas['director'] + ' ' + 
            self.peliculas['descripcion']
        )

        # Vectorización
        self.vectorizador = CountVectorizer().fit_transform(
            self.peliculas['info_combinada']
        )
        self.similitud = cosine_similarity(self.vectorizador)

    def recomendar_peliculas(self, titulo, cantidad=3):
        try:
            # Encontrar índice de la película
            indice = self.peliculas[self.peliculas['titulo'] == titulo].index[0]
            
            # Calcular similitudes
            puntuaciones_similitud = list(enumerate(self.similitud[indice]))
            
            # Ordenar por similitud
            puntuaciones_ordenadas = sorted(
                puntuaciones_similitud, 
                key=lambda x: x[1], 
                reverse=True
            )
            
            # Excluir la película original y tomar las más similares
            recomendaciones = [
                self.peliculas.iloc[ind]['titulo'] 
                for ind, score in puntuaciones_ordenadas[1:cantidad+1]
            ]
            
            return recomendaciones
        
        except IndexError:
            return []

    def crear_interfaz(self):
        root = tk.Tk()
        root.title("Recomendador de Películas")
        root.geometry("400x300")

        # Selector de película
        tk.Label(root, text="Selecciona una película:").pack(pady=10)
        
        self.selector_pelicula = ttk.Combobox(
            root, 
            values=list(self.peliculas['titulo'])
        )
        self.selector_pelicula.pack(pady=10)

        # Botón de recomendación
        tk.Button(
            root, 
            text="Recomendar", 
            command=self.mostrar_recomendaciones
        ).pack(pady=10)

        # Área de resultados
        self.texto_recomendaciones = tk.Text(
            root, height=5, width=40
        )
        self.texto_recomendaciones.pack(pady=10)

        root.mainloop()

    def mostrar_recomendaciones(self):
        pelicula = self.selector_pelicula.get()
        
        if not pelicula:
            messagebox.showwarning("Error", "Selecciona una película")
            return

        recomendaciones = self.recomendar_peliculas(pelicula)
        
        self.texto_recomendaciones.delete('1.0', tk.END)
        
        if recomendaciones:
            self.texto_recomendaciones.insert(
                tk.END, 
                f"Películas similares a {pelicula}:\n\n" + 
                "\n".join(recomendaciones)
            )
        