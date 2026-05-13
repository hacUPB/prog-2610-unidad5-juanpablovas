from pathlib import Path

print("==============================")
print("Explorador Vuelos Aeropuerto Holaya Herrera")


while True:
    print("\nSelecciona la opción del siguiente menú")
    print("1) Explorar directorio")
    print("2) Procesar Bitácoras (.txt)")
    print("3) Analizar Dataset (.csv)")
    print("4) Salir")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        ruta_carpeta = Path("Reto")
        ruta_carpeta.mkdir(parents=True, exist_ok=True)

        print("=== Exploración de Directorio===")
        print("Selecciona las carpetas habilitadas")
        print("1) EOH")

        carpeta_busqueda = int(input("Selecciona la opción de la carpeta: "))

        if carpeta_busqueda == 1:
            ruta = Path("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Reto\\Data\\EOH")

            txt = list(ruta.glob("*.txt"))
            csv = list(ruta.glob("*.csv"))

            # cambiar nombre de csv

            archivos = txt + csv

            if archivos:
                print("\nArchivos encontrados:\n")

                contador = 1

                for archivo in archivos:
                    print(f"{contador}) {archivo.name}")
                    contador += 1
                
                seleccion = int(input("\nSelecciones un archivo: "))

                archivo_seleccionado = archivos[seleccion - 1]

                print("\nArchivo seleccionado:")    
                print(archivo_seleccionado.name)
                
                if archivo_seleccionado.name == "TorredeControl.txt":
                    print("Bitácora de operaciones de la torre de control.")
                
                elif archivo_seleccionado.name == "Mantenimiento.txt":
                    print("Registro técnico de mantenimiento aeroportuario.")
                    
                elif archivo_seleccionado.name == "Incidentes.txt":
                    print("Reporte de incidentes operacionales del aeropuerto.")
                    
                elif archivo_seleccionado.name == "vuelos_olaya.csv":
                    print("Dataset principal de vuelos del Aeropuerto Olaya Herrera.")
                    
                elif archivo_seleccionado.name == "clima_operacional.csv":
                    print("Datos meteorológicos operacionales del aeropuerto.")
                    
                elif archivo_seleccionado.name == "ocupacion_puertas.csv":
                    print("Información sobre uso y ocupación de puertas.")

            else:
                print("\nNo se encontraron archivos")

        print("\nSe volverá al menú principal")

    elif opcion == 2:
        ruta = Path("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Reto\\Data\\EOH")

        bitacoras = list(ruta.glob("*.txt"))

        if bitacoras:
            print("\nBitacoras disponibles:\n")

            contador = 1

            for archivo in bitacoras:
                print(f"{contador}) {archivo.name}")
                contador += 1
                
            seleccion = int(input("\nSelecciones un archivo: "))

            bitacora_seleccionado = bitacoras[seleccion - 1]

            print("\nBitacora seleccionada:")    
            print(bitacora_seleccionado.name)

        else:
            print("\nNo se encontraron archivos")

        while True:
            print("\n¿Que deseas hacer con el texto")
            print("1) Mostrar el contenido")
            print("2) Conocer la cantidad de lineas que contiene")
            print("3) Conocer la cantidad de palabras que contiene")
            print("4) Top 5 de palabras repetidas")
            print("5) volver al menú principal")

            textos = int(input("\nSelecciona la opcion: "))
        
            # mostar el contenido
            with open(bitacora_seleccionado, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            if textos == 1:
                print("\nContenido del archivo")
                print(contenido)
        
            elif textos == 2:
                lineas = contenido.splitlines()
                cantidad_lineas = len(lineas)
            
                print("\nCantidad total de líneas:")
                print(cantidad_lineas)
            
            elif textos == 3:
                palabras = contenido.split()
                cantidad_palabras = len(palabras)
                print("\nCantidad total de palabras:")
                print(cantidad_palabras)
            
            elif textos == 4:
                frecuencia = {}

                palabras = contenido.split()

                for palabra in palabras:
                    palabra = palabra.lower()

                    if palabra in frecuencia:
                        frecuencia[palabra] += 1

                    else:
                        frecuencia[palabra] = 1

                print("\nTop 5 palabras más repetidas:\n")

                for i in range(5):
                    palabra_mas_repetida = max(frecuencia, key=frecuencia.get)
                    cantidad = frecuencia[palabra_mas_repetida]
                    print(palabra_mas_repetida, ":", cantidad)
                    del frecuencia[palabra_mas_repetida]
            
            elif textos == 5:
                break

        # Opción 3
    elif opcion == 3:
        print("\n[ ANÁLISIS DE DATASET CSV ]")
        pass

        # Opción 4
    elif opcion == 4:
        print("\nSaliendo del sistema...")
        break

        # Opción inválida
    else:
        print("\nERROR: Opción inválida")
        pass
