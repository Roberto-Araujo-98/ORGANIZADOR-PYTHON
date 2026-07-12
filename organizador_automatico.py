import os
import shutil
from datetime import datetime

# 1. DICCIONARIO AMPLIADO
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.md'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.m4a', '.wma'],
    'Programacion_Codigo': ['.java', '.py', '.sql', '.js', '.ts', '.html', '.css', '.sh', '.cpp', '.c', '.rs'],
    'Programas_Instaladores': ['.exe', '.msi', '.deb', '.zip', '.rar', '.tar.gz'],
    'Aplicaciones_Moviles': ['.apk', '.aab']
}

# ⚠️ LA RUTA SE QUEDA AQUÍ ARRIBA PARA QUE TODO EL SCRIPT LA PUEDA USAR
RUTA_A_MONITOREAR = "C:/Users/USER/Downloads" 

def registrar_log(mensaje):
    """Guarda un registro de lo que hace el script en un archivo txt dentro de Downloads."""
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 📌 CON ESTO UNIMOS LA RUTA DE DOWNLOADS CON EL ARCHIVO DE TEXTO
    ruta_del_log = os.path.join(RUTA_A_MONITOREAR, "historial_cambios.txt")
    
    with open(ruta_del_log, "a", encoding="utf-8") as archivo_log:
        archivo_log.write(f"[{fecha_hora}] {mensaje}\n")

def ordenar_silencioso(ruta_objetivo):
    if not os.path.exists(ruta_objetivo):
        return

    os.chdir(ruta_objetivo)
    archivos_encontrados = os.listdir()
    
    if not archivos_encontrados:
        return

    conteo_movidos = 0
    registrar_log(f"--- Iniciando escaneo automático en: {ruta_objetivo} ---")

    for archivo in archivos_encontrados:
        # Evita mover carpetas, los scripts y el propio archivo de historial
        if os.path.isdir(archivo) or archivo.startswith('organizador') or archivo == 'historial_cambios.txt':
            continue
            
        _, ext = os.path.splitext(archivo)
        ext = ext.lower()
        
        movido = False
        for carpeta, extensiones_validas in EXTENSIONES.items():
            if ext in extensiones_validas:
                if not os.path.exists(carpeta):
                    os.makedirs(carpeta)
                
                shutil.move(archivo, os.path.join(carpeta, archivo))
                registrar_log(f"Movido: {archivo} -> {carpeta}")
                conteo_movidos += 1
                movido = True
                break
        
        if not movido and ext != '':
            if not os.path.exists('Otros'):
                os.makedirs('Otros')
            shutil.move(archivo, os.path.join('Otros', archivo))
            registrar_log(f"Movido (Sin clasificar): {archivo} -> Otros")
            conteo_movidos += 1

    if conteo_movidos > 0:
        registrar_log(f"Escaneo finalizado. Se organizaron {conteo_movidos} archivos.\n")

if __name__ == "__main__":
    ordenar_silencioso(RUTA_A_MONITOREAR)