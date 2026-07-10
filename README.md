# File Organizer CLI 📁🛠️

Un script interactivo en Python para automatizar la limpieza y ordenamiento de cualquier carpeta en tu sistema operativo basándose en las extensiones de los archivos.

## ✨ Características
- **Interactivo (CLI):** Pide la ruta de la carpeta directamente en la terminal antes de actuar.
- **Validación Robusta:** Verifica si la ruta ingresada es real y si corresponde a un directorio. No se cierra si cometes un error de escritura.
- **Clasificación inteligente:** Agrupa automáticamente archivos en carpetas específicas (`Documentos`, `Imagenes`, `Videos`, `Programas_Instaladores`).
- **Cajón de Sastre:** Mueve los formatos desconocidos o poco comunes a una carpeta llamada `Otros` para mantener el espacio limpio.

## 🚀 Cómo usarlo

1. Asegúrate de tener instalado **Python 3.x**.
2. Descarga o clona este repositorio.
3. Abre tu terminal en la carpeta del script y ejecútalo:
   ```bash
   python organizador.py

Introduce la ruta absoluta de la carpeta que deseas organizar (por ejemplo: C:/Users/TuUsuario/Downloads) o escribe salir para cancelar.

📁 Ejemplo de Organización
Antes de ejecutar el script, tus archivos sueltos se verán así. Al terminar, se habrán movido a sus respectivos directorios limpios:

📂 MiCarpeta/
 ├── 📄 clase_algebra.pdf      ➔   📂 Documentos/clase_algebra.pdf
 ├── 📷 captura.png            ➔   📂 Imagenes/captura.png
 ├── 🎬 intro_proyecto.mp4     ➔   📂 Videos/intro_proyecto.mp4
 └── ⚙️ node_installer.msi     ➔   📂 Programas_Instaladores/node_installer.msi


 ---

> 💡 **Tip final:** Para que se vea aún mejor en tu perfil principal, asegúrate de ponerle etiquetas (tags) a tu repositorio de GitHub como `python`, `automation`, `cli` y `script`. ¡A subirlo!