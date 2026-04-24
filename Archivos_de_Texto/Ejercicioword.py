"""
1. Leer el nuevo archivo
2. Leer todo el documento en forma de lista
3. Imprimir la primera letra de cada item
"""
archivo = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\ejericicioword.txt","r",encoding="utf-8")

# first_lectura = archivo.read()
# print(f"Punto 1\n {first_lectura}")

# second_lectura = archivo.readlines()
# print(second_lectura)
i = 0

thirth_lectura = archivo.readlines()

for dato in thirth_lectura:
    print(dato[0])


archivo.close()