# 📁 Organizador de Archivos Personalizado
 Un script de Python simple y eficaz para organizar tus archivos de forma automática en carpetas personalizadas, basándose en sus extensiones. Ideal para mantener ordenado tu escritorio o cualquier carpeta de descargas.

## ✨ Características
* Organización Personalizada: Define tus propias reglas de organización asociando extensiones de archivo (.pdf, .jpg, .mp3) a nombres de carpetas.

* Interfaz Gráfica (GUI): Una interfaz intuitiva construida con tkinter que facilita la selección de la carpeta y la gestión de reglas sin necesidad de editar código.

* Detección de Carpetas Existentes: El programa te sugiere los nombres de carpetas ya creadas en el directorio, para que puedas añadirles más extensiones sin esfuerzo.

* Manejo de Archivos no Clasificados: Mueve automáticamente los archivos sin reglas definidas a una carpeta "Otros".

## 🛠️ Tecnologías Utilizadas
* Python: Lenguaje de programación principal.

* Tkinter: Biblioteca estándar de Python para la interfaz gráfica de usuario.

* Módulo os: Para interactuar con el sistema operativo y gestionar rutas de archivos y directorios.

* Módulo shutil: Para operaciones de alto nivel sobre archivos, como mover y copiar.

## ⚙️ Instalación y Uso
* Sigue estos pasos para poner en marcha el organizador de archivos:

1. Clonar el Repositorio.

2. Ejecutar la Aplicación:
No necesitas instalar dependencias externas, ya que el proyecto usa bibliotecas estándar de Python. Simplemente ejecuta el script principal:

* Cómo usar la GUI:

1. Haz clic en el botón "..." para seleccionar la carpeta que deseas organizar.

2. En la sección "Añadir nueva regla", elige un nombre de carpeta y una extensión de archivo. Puedes escribir tus propios valores o seleccionarlos de los menús desplegables.

3. Haz clic en "Añadir Extensión" para guardar la regla.

4. Repite el proceso para todas las reglas que necesites.

3. Finalmente, haz clic en el botón "Organizar" para iniciar el proceso. 
