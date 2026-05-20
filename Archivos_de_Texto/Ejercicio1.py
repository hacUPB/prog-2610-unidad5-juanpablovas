#Apertura o creacion de un archivo
mi_archivo = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\saludo.txt","a")
#En la anterior linea se dió la dirección donde quiero guardar el archivo

x = 0
for i in range(5):
    x = x + 1
    mi_archivo.write(f"\n{x}")
    
mi_archivo.close()

