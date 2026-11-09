import os
import platform

    
#Procesador donde se ejecuta el programa
procesador = platform.processor()
print(f"Procesador: {procesador}")
    
#Sistema operativo y versión
sistema = platform.system()
version = platform.release()
print(f"Sistema Operativo: {sistema} (Versión: {version})")
    
#Nombre del host
host = platform.node()
print(f"Nombre del host: {host}")
    
#Directorio actual de trabajo
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

