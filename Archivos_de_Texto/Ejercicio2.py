archivo = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\log.txt","a") #El archivo se crea en la raiz del repositorio
texto = input("Ingresa una frase: ")
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura: "))
archivo.write(f"{texto}\n")
archivo.write(f"Edad: {edad}\n")
archivo.write(f"Estatura: {estatura}\n")

archivo.close()