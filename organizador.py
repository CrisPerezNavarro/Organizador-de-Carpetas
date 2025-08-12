import os
import shutil
import tkinter as tk
from tkinter import messagebox

#  Organiza los archivos en un directorio dado según una configuración personalizada.
def organizar_archivos(directorio_a_organizar, extensiones_personalizadas):
  
    try:
        # Usa os.scandir() para una iteración más eficiente sobre los archivos del directorio.
        with os.scandir(directorio_a_organizar) as entries:
            # Itera sobre cada entrada (archivo o carpeta) en el directorio.
            for entry in entries:
                # Solo procesa archivos, ignora las subcarpetas.
                if entry.is_file():
                    # Obtiene la extensión del archivo y la convierte a minúsculas para
                    # asegurar que la comparación sea insensible a mayúsculas y minúsculas.
                    extension_archivo = os.path.splitext(entry.name)[1].lower()
                    
                    encontrado = False  # Bandera para saber si el archivo ha sido clasificado.
                    
                    # Itera sobre las reglas de organización definidas por el usuario.
                    for carpeta, extensiones in extensiones_personalizadas.items():
                        # Comprueba si la extensión del archivo está en la lista de extensiones
                        # para la carpeta actual.
                        if extension_archivo in extensiones:
                            # Construye la ruta de destino de la nueva carpeta.
                            ruta_destino_carpeta = os.path.join(directorio_a_organizar, carpeta)
                            
                            # Si la carpeta de destino no existe, la crea.
                            if not os.path.exists(ruta_destino_carpeta):
                                os.makedirs(ruta_destino_carpeta)

                            # Mueve el archivo a la carpeta de destino.
                            shutil.move(entry.path, os.path.join(ruta_destino_carpeta, entry.name))
                            print(f"Archivo {entry.name} movido a {carpeta}")
                            encontrado = True
                            break  # Rompe el bucle una vez que el archivo ha sido movido.
                    
                    # Si la extensión del archivo no coincide con ninguna regla, lo mueve a "Otros".
                    if not encontrado:
                        ruta_otros = os.path.join(directorio_a_organizar, "Otros")
                        # Si la carpeta "Otros" no existe, la crea.
                        if not os.path.exists(ruta_otros):
                            os.makedirs(ruta_otros)
                        # Mueve el archivo a la carpeta "Otros".
                        shutil.move(entry.path, os.path.join(ruta_otros, entry.name))
                        print(f"Archivo {entry.name} movido a Otros")
        
        # Muestra un mensaje de éxito una vez que la organización ha terminado.
        messagebox.showinfo("Éxito", "La carpeta ha sido organizada correctamente.")
    
    except Exception as e:
        # Captura cualquier error que pueda ocurrir durante el proceso y muestra un mensaje de error.
        messagebox.showerror("Error", f"Ocurrió un error: {e}")