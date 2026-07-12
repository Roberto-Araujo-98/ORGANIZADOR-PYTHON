import os
import shutil
from datetime import datetime

# Diccionario que define qué extensiones van a qué carpetas
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.wma'],
    'Programacion_Codigo': ['.java', '.py', '.sql', '.js', '.ts', '.html', '.css', '.sh', '.cpp', '.c', '.rs'],
    'Programas_Instaladores': ['.exe', '.msi', '.deb', '.zip', '.rar', '.tar.gz'],
    'Aplicaciones_Moviles': ['.apk', '.aab']
}

def ordenar_carpeta(ruta_objetivo):
    if not os.path.exists(ruta_objetivo):
        print("❌ La ruta no existe.")
        return

    os.chdir(ruta_objetivo)
    archivos_encontrados = os.listdir()
    
    conteo_movidos = 0

    for archivo in archivos_encontrados:
        # 🔥 FILTRO DE SEGURIDAD: Ignora carpetas y evita que el script se mueva a sí mismo
        if os.path.isdir(archivo) or archivo.startswith('organizador'):
            continue
            
        _, ext = os.path.splitext(archivo)
        ext = ext.lower()
        
        movido = False
        for carpeta, extensiones_validas in EXTENSIONES.items():
            if ext in extensiones_validas:
                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)
                
                shutil.move(archivo, os.path.join(carpeta, archivo))
                print(f"📦 Movido: {archivo} -> {carpeta}")
                conteo_movidos += 1
                movido = True
                break
        
        if not movido and ext != '':
            if not os.path.exists('Otros'):
                os.makedirs('Otros')
            shutil.move(archivo, os.path.join('Otros', archivo))
            print(f"📦 Movido (Sin clasificar): {archivo} -> Otros")
            conteo_movidos += 1

    print(f"\n✨ ¡Limpieza terminada! Se organizaron {conteo_movidos} archivos.\n")

if __name__ == "__main__":
    print("--- ORGANIZADOR DE CARPETAS INTERACTIVO ---")
    
    while True:
        # El .strip(' "\'') elimina espacios y comillas dobles o simples que se peguen por error
        ruta = input("Introduce la ruta de la carpeta que quieres organizar (o escribe 'salir'): ").strip().strip('"').strip("'")
        
        if ruta.lower() == 'salir':
            print("👋 Proceso cancelado por el usuario.")
            break
            
        if os.path.exists(ruta):
            if os.path.isdir(ruta):
                print(f"\n🔍 Iniciando ordenamiento en: {os.path.abspath(ruta)}")
                ordenar_carpeta(ruta)
                break 
            else:
                print("❌ Error: La ruta ingresada es un archivo, no una carpeta. Intenta de nuevo.\n")
        else:
            print("❌ Error: La ruta no existe. Asegúrate de escribirla bien (Ej: C:/Users/USER/Downloads)\n")