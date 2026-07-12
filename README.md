# 📂 File Organizer Automation Suite

Una suite de herramientas eficientes en Python diseñadas para la clasificación, gestión y ordenamiento automatizado de archivos en directorios locales. El sistema está optimizado para mitigar el impacto en el rendimiento de memoria mediante una arquitectura basada en eventos temporizados por el sistema operativo, evitando bucles infinitos de monitoreo en segundo plano.

### 🔄 ¿Cómo funciona el flujo de ordenamiento?

```text
📂 Carpeta_Origen/ (Descargas / Ruta seleccionada)
 ├── 📄 clase_algebra.pdf     ➔   📂 Documentos/clase_algebra.pdf
 ├── 📷 captura.png           ➔   📂 Imagenes/captura.png
 ├── 🎬 intro_proyecto.mp4    ➔   📂 Videos/intro_proyecto.mp4
 └── ⚙️ node_installer.msi    ➔   📂 Programas_Instaladores/node_installer.msi
```

---

## 1. 🛠️ Organizador Manual Interactivo (`organizador.py`)

Este script proporciona una interfaz de línea de comandos (CLI) interactiva que permite al usuario especificar de forma dinámica cualquier ruta del sistema de archivos para su ordenamiento inmediato.

### Características Técnicas
* **Mecanismo de Parsing Riguroso:** Implementa limpieza de cadenas mediante `.strip()` para remover espacios en blanco y comillas dobles (`"`) o simples (`'`) residuales que suelen añadirse de forma automática al arrastrar o copiar rutas desde el Explorador de Windows.
* **Filtro de Autoprotección:** Incorpora una validación condicional (`archivo.startswith('organizador')`) para evitar que el script manipule o desplace sus propios archivos fuente en caso de ser ejecutado dentro de su mismo directorio raíz.
* **Arquitectura de Flujo:** Utiliza un bucle interactivo controlado que valida la existencia del directorio (`os.path.exists`) y su integridad como carpeta (`os.path.isdir`) antes de proceder con el mapeo.

---

## 2. 🤖 Organizador Autónomo Programado (`organizador_automatico.py`)

Diseñado específicamente para ejecuciones desatendidas y automatizadas a través del sistema operativo. Funciona de manera silenciosa (sin interfaz ni prints de consola) y genera reportes de auditoría en tiempo real.

### Características Técnicas
* **📋 Persistencia de Registros (Logging):** Integra la función `registrar_log` que escribe de forma síncrona el historial de transferencias con marcas de tiempo formateadas en un archivo llamado `historial_cambios.txt`.
* **📍 Rutado Absoluto:** Utiliza `os.path.join` vinculando una constante global de destino (`RUTA_A_MONITOREAR`), garantizando que la bitácora y las subcarpetas se gestionen exclusivamente en el directorio de descargas (`Downloads`), independientemente del contexto o la ubicación desde donde Windows invoque la ejecución inicial.
* **🔒 Exclusión de Archivos Críticos:** Discrimina tanto el archivo de bitácora como los ejecutables de la suite para asegurar la atomicidad del proceso de ordenamiento.

---

## ⏰ 3. Automatización con el Programador de Tareas de Windows

Para optimizar el uso de recursos de hardware, la ejecución del script autónomo se delega al kernel de Windows mediante tareas programadas cronológicamente (mañana y noche), evitando hilos persistentes o daemons consumiendo memoria RAM innecesaria.

### Instrucciones de Despliegue

1. Abra la consola de comandos de Windows (`Win + R`), escriba **`taskschd.msc`** y presione **Enter**.
2. En el panel de acciones derecho, seleccione **Crear tarea básica...**.
3. Asigne un identificador técnico (Ej. `Organizador_Descargas_Automático`).
4. En **Desencadenador**, defina la periodicidad como **Diariamente** e inicialice el marcador a las `08:00:00 AM`.
5. En **Acción**, seleccione **Iniciar un programa** y complete los parámetros con rutas absolutas:
   * **Programa o script:** Ingrese la ruta del lanzador global de Python del sistema:
     ```text
     C:\WINDOWS\py.exe
     ```
   * **Agregar argumentos (opcional):** Ingrese la ruta absoluta hacia el script autónomo:
     ```text
     D:\PROYECTOS-CODE\Python-proyecto\ORGANIZADOR-PYTHON\organizador_automatico.py
     ```
   * **Iniciar en (opcional):** Dejar vacío (el script autogestiona el contexto de los directorios).
6. Finalice la creación de la tarea básica.
7. **⚙️ Turno Nocturno:** Para añadir la ejecución nocturna, haga doble clic sobre la tarea creada dentro de la **Biblioteca del Programador de Tareas**, navegue a la pestaña **Desencadenadores**, haga clic en **Nuevo...** y defina el segundo disparador diariamente a las `08:00:00 PM`.

---

## 💻 4. Requerimientos del Sistema y Especificaciones

### Entorno de Execución
* **Sistema Operativo:** Microsoft Windows 10 / Windows 11.
* **Intérprete:** Python 3.10 o superior.

### Dependencias de la Biblioteca Estándar
El proyecto no requiere gestores de paquetes externos (`pip`) al basarse estrictamente en módulos nativos integrados de Python:
* `os`: Manipulación de rutas, cambios de directorio operativo y verificación de descriptores.
* `shutil`: Operaciones de alto nivel para la transferencia y desplazamiento atómico de archivos.
* `datetime`: Captura y formateo de estructuras temporales del sistema para logs.

### 📊 Matriz de Clasificación por Extensiones

Los archivos se distribuyen de forma automatizada en las siguientes estructuras de directorios según su extensión:

| Directorio Destino | Emojis Asociados | Extensiones Soportadas |
| :--- | :---: | :--- |
| **Documentos** | 📄 | `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, `.md` |
| **Imagenes** | 📷 | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg` |
| **Videos** | 🎬 | `.mp4`, `.mkv`, `.avi`, `.mov` |
| **Audio** | 🎵 | `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.wma` |
| **Programacion_Codigo** | 💻 | `.java`, `.py`, `.sql`, `.js`, `.ts`, `.html`, `.css`, `.sh`, `.cpp`, `.c`, `.rs` |
| **Programas_Instaladores** | ⚙️ | `.exe`, `.msi`, `.deb`, `.zip`, `.rar`, `.tar.gz` |
| **Aplicaciones_Moviles** | 📱 | `.apk`, `.aab` |
| **Otros** | 📦 | Cualquier archivo con extensión no catalogada en la matriz anterior. |