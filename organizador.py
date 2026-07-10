import os
import shutil

# Diccionario que define qué extensiones van a qué carpetas
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Programas_Instaladores': ['.exe', '.msi', '.deb', '.zip', '.rar', '.tar.gz']
}

def ordenar_carpeta(ruta_objetivo):
    # Asegurarnos de que la ruta existe
    if not os.path.exists(ruta_objetivo):
        print("La ruta no existe.")
        return

    # Cambiar al directorio objetivo
    os.chdir(ruta_objetivo)
    
    # Listar todos los archivos sueltos
    for archivo in os.listdir():
        # Ignorar si es una carpeta o el propio script
        if os.path.isdir(archivo) or archivo == 'organizador.py':
            continue
            
        # Extraer la extensión del archivo en minúsculas
        _, ext = os.path.splitext(archivo)
        ext = ext.lower()
        
        # Buscar a qué categoría pertenece
        movido = False
        for carpeta, extensiones_validas in EXTENSIONES.items():
            if ext in extensiones_validas:
                # Crear la carpeta si no existe
                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)
                
                # Mover el archivo
                shutil.move(archivo, os.path.join(carpeta, archivo))
                print(os.path.join("Movido:", archivo, "->", carpeta))
                movido = True
                break
        
        # Opcional: Mandar a "Otros" si no coincide con ninguna extensión
        if not movido and ext != '':
            if not os.path.exists('Otros'):
                os.makedirs('Otros')
            shutil.move(archivo, os.path.join('Otros', archivo))

if __name__ == "__main__":
    # Puedes poner '.' para ordenar la carpeta actual donde ejecutes el script,
    # o poner una ruta directa como 'C:/Users/TuUsuario/Downloads'
    ruta = '.' 
    print(os.path.join("Iniciando ordenamiento en:", os.path.abspath(ruta)))
    ordenar_carpeta(ruta)
    print("¡Carpeta organizada con éxito!")