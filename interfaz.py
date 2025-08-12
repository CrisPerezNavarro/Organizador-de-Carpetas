import tkinter as tk
from tkinter import filedialog, messagebox
from organizador import organizar_archivos
from tkinter import ttk
import os

# Diccionario para guardar las reglas de organización
configuracion_usuario = {}

# Configuraciones de ejemplo para el Combobox de extensiones
extensiones_disponibles = ['.pdf', '.doc', '.docx', '.txt', '.pptx', '.jpg', '.png', '.mp4', '.mp3', '.zip']

def actualizar_combo_carpetas(directorio_a_organizar):
    """Actualiza el ComboBox de nombres de carpetas con las carpetas existentes."""
    nombres_carpetas_existentes = [d for d in os.listdir(directorio_a_organizar) if os.path.isdir(os.path.join(directorio_a_organizar, d))]
    combo_nombre_carpeta['values'] = nombres_carpetas_existentes
    combo_nombre_carpeta.set('')

def seleccionar_carpeta():
    directorio_elegido = filedialog.askdirectory()
    if directorio_elegido:
        ruta_entrada.delete(0, tk.END)
        ruta_entrada.insert(0, directorio_elegido)
        actualizar_combo_carpetas(directorio_elegido) # Llama a la función para actualizar el ComboBox

def agregar_regla_gui():
    nombre_carpeta = combo_nombre_carpeta.get().strip()
    # Aquí se corrige la variable
    extension_seleccionada = combo_extensiones.get().strip().lower()
    
    if not nombre_carpeta:
        messagebox.showwarning("Advertencia", "El nombre de la carpeta no puede estar vacío.")
        return
    if not extension_seleccionada:
        messagebox.showwarning("Advertencia", "Por favor, selecciona o ingresa una extensión.")
        return

    # Si la carpeta ya existe en la configuración, agrega la nueva extensión
    if nombre_carpeta in configuracion_usuario:
        if extension_seleccionada not in configuracion_usuario[nombre_carpeta]:
            configuracion_usuario[nombre_carpeta].append(extension_seleccionada)
    else:
        # Si la carpeta es nueva, crea una nueva entrada en el diccionario
        configuracion_usuario[nombre_carpeta] = [extension_seleccionada]
    
    actualizar_listbox()
    
    # limpiar
    combo_nombre_carpeta.set('')
    combo_extensiones.set('')

    messagebox.showinfo("Regla añadida", f"Regla para '{nombre_carpeta}' actualizada con '{extension_seleccionada}'.")

def eliminar_regla_gui():
    try:
        seleccion_index = listbox_reglas.curselection()[0]
        regla_a_eliminar = listbox_reglas.get(seleccion_index)
        
        # Encuentra el nombre de la carpeta para eliminar
        nombre_carpeta_a_eliminar = regla_a_eliminar.split(':')[0]
        del configuracion_usuario[nombre_carpeta_a_eliminar]
        listbox_reglas.delete(seleccion_index)

        messagebox.showinfo("Regla eliminada", f"Regla para '{nombre_carpeta_a_eliminar}' eliminada.")

    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una regla para eliminar.")

def actualizar_listbox():
    listbox_reglas.delete(0, tk.END)
    for nombre_carpeta, extensiones in configuracion_usuario.items():
        listbox_reglas.insert(tk.END, f"{nombre_carpeta}: {', '.join(extensiones)}")

def iniciar_organizacion():
    directorio_a_organizar = ruta_entrada.get()
    if not directorio_a_organizar:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una carpeta.")
        return
    
    if not configuracion_usuario:
        messagebox.showwarning("Advertencia", "Por favor, añade al menos una regla de organización.")
        return

    organizar_archivos(directorio_a_organizar, configuracion_usuario)

# --- Configuración de la interfaz ---
ventana = tk.Tk()
ventana.title("Organizador de Archivos Personalizado")
ventana.geometry("600x450")

# Frame principal
frame_principal = tk.Frame(ventana, padx=10, pady=10)
frame_principal.pack(fill="both", expand=True)

# Sección de selección de carpeta
frame_ruta = tk.Frame(frame_principal)
frame_ruta.pack(pady=10, fill="x")
tk.Label(frame_ruta, text="Carpeta a organizar:").pack(side=tk.LEFT)
ruta_entrada = tk.Entry(frame_ruta, width=40)
ruta_entrada.pack(side=tk.LEFT, padx=5)
boton_seleccionar = tk.Button(frame_ruta, text="...", command=seleccionar_carpeta)
boton_seleccionar.pack(side=tk.LEFT)

# Sección para añadir reglas
frame_reglas = tk.Frame(frame_principal, bd=2, relief="groove", padx=10, pady=10)
frame_reglas.pack(fill="x", pady=10)
tk.Label(frame_reglas, text="Añadir nueva regla de organización").pack(pady=(0, 5))

# Input para el nombre de la carpeta (ComboBox)
tk.Label(frame_reglas, text="Nombre de la Carpeta:").pack()
combo_nombre_carpeta = ttk.Combobox(frame_reglas)
combo_nombre_carpeta.pack()

# Input para las extensiones (ComboBox)
tk.Label(frame_reglas, text="Extensión de Archivo:").pack()
combo_extensiones = ttk.Combobox(frame_reglas, values=extensiones_disponibles, state="normal")
combo_extensiones.pack()

boton_agregar_regla = tk.Button(frame_reglas, text="Añadir Extensión", command=agregar_regla_gui)
boton_agregar_regla.pack(pady=5, side=tk.LEFT, padx=5)

# Botón para eliminar reglas
boton_eliminar_regla = tk.Button(frame_reglas, text="Eliminar Carpeta", command=eliminar_regla_gui)
boton_eliminar_regla.pack(pady=5, side=tk.RIGHT, padx=5)


# Sección de visualización de reglas
tk.Label(frame_principal, text="Reglas actuales:").pack(pady=(10, 0))
listbox_reglas = tk.Listbox(frame_principal, width=70, height=5)
listbox_reglas.pack(pady=5, fill="x")

# Botón de iniciar
boton_organizar = tk.Button(frame_principal, text="Organizar", command=iniciar_organizacion, bg="green", fg="white", font=("Helvetica", 12))
boton_organizar.pack(pady=10)

ventana.mainloop()