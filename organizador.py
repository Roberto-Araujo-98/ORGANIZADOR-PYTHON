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
        # Ignorar si es una carpeta
        if os.path.isdir(archivo):
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
                print(f"Movido: {archivo} -> {carpeta}")
                movido = True
                break
        
        # Opcional: Mandar a "Otros" si tiene extensión pero no coincide con ninguna del mapa
        if not movido and ext != '':
            if not os.path.exists('Otros'):
                os.makedirs('Otros')
            shutil.move(archivo, os.path.join('Otros', archivo))

if __name__ == "__main__":
    print("--- ORGANIZADOR DE CARPETAS AUTOMÁTICO ---")
    
    # Bucle infinito para pedir la ruta hasta que pongan una válida
    while True:
        ruta = input("Introduce la ruta de la carpeta que quieres organizar (o escribe 'salir'): ").strip()
        
        # Opción por si te arrepientes y quieres cerrar el script
        if ruta.lower() == 'salir':
            print("Proceso cancelado por el usuario.")
            break
            
        # Validar si la ruta que escribió el usuario realmente existe en la PC
        if os.path.exists(ruta):
            if os.path.isdir(ruta):
                print(f"\nIniciando ordenamiento en: {os.path.abspath(ruta)}")
                ordenar_carpeta(ruta)
                print("¡Carpeta organizada con éxito!\n")
                break # Rompe el bucle porque ya terminó con éxito
            else:
                print("❌ Error: La ruta ingresada existe, pero es un archivo, no una carpeta. Intenta de nuevo.\n")
        else:
            print("❌ Error: La ruta no existe. Asegúrate de escribirla bien (Ej: C:/Users/USER/Downloads)\n")