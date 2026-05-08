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

        carpeta_busqueda = int(input("Selecciona la opcioón de la carpeta: "))

        if carpeta_busqueda == 1:
            ruta = Path("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Reto\\Data\\EOH")

            archivos = list(ruta.glob("*.txt"))

            if archivos:
                print("\nArchivos encontrados:\n")
                for eoh in archivos:
                    print(eoh.name)
            
            else:
                print("\no se encontraron archivos")


    elif opcion == 2:
        print("\n[ PROCESAMIENTO DE BITÁCORAS ]")
        pass

        # Opción 3
    elif opcion == 3:
        print("\n[ ANÁLISIS DE DATASET CSV ]")
        pass

        # Opción 4
    elif opcion == 4:
        print("\nSaliendo del sistema...")
        pass
        break

        # Opción inválida
    else:
        print("\nERROR: Opción inválida")
        pass
