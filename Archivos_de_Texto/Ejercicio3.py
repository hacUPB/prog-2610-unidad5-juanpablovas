from random import randint

lista = []
for i in range(50):
    lista.append(randint(0, 100))

maximo = str(max(lista))
minimo = str(min(lista))
prom = str(sum(lista)/len(lista))

file_datos = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\datos.txt", "w",encoding="utf-8")
file_datos.write("El valor máximo es: " + maximo + "\n")
file_datos.write("El valor mínimo es: " + minimo + "\n")
file_datos.write("El promedio es: " + prom + "\n")
file_datos.close()
print("Archivo creado con éxito. Revisa tu carpeta.")