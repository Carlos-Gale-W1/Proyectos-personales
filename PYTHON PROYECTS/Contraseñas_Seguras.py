import random
import string
import pyperclip

def generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    """
    Genera una contraseña segura con los parámetros especificados.
    
    :param longitud: Longitud de la contraseña
    :param mayusculas: Incluir letras mayúsculas
    :param numeros: Incluir números
    :param simbolos: Incluir símbolos especiales
    :return: Contraseña generada
    """
    # Definir conjuntos de caracteres
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase if mayusculas else ''
    digitos = string.digits if numeros else ''
    caracteres_especiales = string.punctuation if simbolos else ''
    
    # Combinar todos los caracteres
    todos_caracteres = letras_minusculas + letras_mayusculas + digitos + caracteres_especiales
    
    # Generar contraseña
    contrasena = []
    
    # Asegurar al menos un carácter de cada tipo seleccionado
    if mayusculas:
        contrasena.append(random.choice(letras_mayusculas))
    if numeros:
        contrasena.append(random.choice(digitos))
    if simbolos:
        contrasena.append(random.choice(caracteres_especiales))
    
    # Rellenar el resto de la contraseña
    for _ in range(longitud - len(contrasena)):
        contrasena.append(random.choice(todos_caracteres))
    
    # Mezclar aleatoriamente
    random.shuffle(contrasena)
    
    return ''.join(contrasena)

def menu_generador_contrasenas():
    while True:
        print("\n--- Generador de Contraseñas Seguras ---")
        print("1. Generar Contraseña Predeterminada")
        print("2. Personalizar Contraseña")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            contrasena = generar_contrasena()
            print(f"\nContraseña generada: {contrasena}")
            pyperclip.copy(contrasena)
            print("Contraseña copiada al portapapeles.")
        
        elif opcion == '2':
            while True:
                try:
                    longitud = int(input("Ingrese la longitud de la contraseña: "))
                    if longitud < 4:
                        print("La longitud debe ser al menos 4 caracteres.")
                        continue
                    
                    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
                    numeros = input("¿Incluir números? (s/n): ").lower() == 's'
                    simbolos = input("¿Incluir símbolos especiales? (s/n): ").lower() == 's'
                    
                    contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
                    print(f"\nContraseña generada: {contrasena}")
                    pyperclip.copy(contrasena)
                    print("Contraseña copiada al portapapeles.")
                    break
                
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")
        
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_generador_contrasenas()