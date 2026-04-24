'''
# Forma antigua
f = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\datos1.txt", "r")
contenido = f.read()
f.close()

# Forma moderna (Recomendada)
with open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\datos1.txt", "r") as f:
    contenido = f.read()
# ¡Ya está cerrado automáticamente aquí!
'''

nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")

# Contexto de escritura
with open(nombre_archivo, 'w+') as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0)
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())

# Contexto de lectura
# with open(nombre_archivo, 'r') as archivo:
#    print("\n--- Leyendo tu archivo ---")
#   print(archivo.read())