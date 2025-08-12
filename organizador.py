import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Asegúrate de que la función acepte dos argumentos
def organizar_archivos(directorio_a_organizar, extensiones_personalizadas):
    """
    Organiza los archivos en un directorio dado según una configuración personalizada.
    """
    try:
        with os.scandir(directorio_a_organizar) as entries:
            for entry in entries:
                if entry.is_file():
                    extension_archivo = os.path.splitext(entry.name)[1].lower()
                    
                    encontrado = False
                    for carpeta, extensiones in extensiones_personalizadas.items():
                        if extension_archivo in extensiones:
                            ruta_destino_carpeta = os.path.join(directorio_a_organizar, carpeta)
                            if not os.path.exists(ruta_destino_carpeta):
                                os.makedirs(ruta_destino_carpeta)

                            shutil.move(entry.path, os.path.join(ruta_destino_carpeta, entry.name))
                            print(f"Archivo {entry.name} movido a {carpeta}")
                            encontrado = True
                            break
                    
                    if not encontrado:
                        ruta_otros = os.path.join(directorio_a_organizar, "Otros")
                        if not os.path.exists(ruta_otros):
                            os.makedirs(ruta_otros)
                        shutil.move(entry.path, os.path.join(ruta_otros, entry.name))
                        print(f"Archivo {entry.name} movido a Otros")
        
        messagebox.showinfo("Éxito", "La carpeta ha sido organizada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")