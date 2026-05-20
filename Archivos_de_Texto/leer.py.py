fp = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\Ejercicio1.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
print("Primera lectura:", datos_1)

# datos_2 = fp.read(5)
# print("Segunda lectura:", datos_2)
fp.close()