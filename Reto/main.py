from pathlib import Path
import matplotlib.pyplot as plt
import csv

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
            print("5) Identificar patrones")
            print("6) Gráfico secuencia de palabras claves")
            print("7) Gráfico distribución de longitud de lineas")
            print("8) volver al menú principal")

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
                lineas = contenido.splitlines()

                aerolineas = {
                    "SATENA": 0,
                    "Clic": 0,
                    "LATAM": 0,
                    "Avianca": 0
                }

                for linea in lineas:

                    if "SATENA" in linea:
                        aerolineas["SATENA"] += 1

                    if "Clic" in linea:
                        aerolineas["Clic"] += 1

                    if "LATAM" in linea:
                        aerolineas["LATAM"] += 1

                    if "Avianca" in linea:
                        aerolineas["Avianca"] += 1

                print("\nFrecuencia de aerolíneas:")

                for nombre in aerolineas:
                    print(nombre, ":", aerolineas[nombre])

                print("\nMatriculas colombianas encontradas:")

                matriculas_hk = {}

                palabras = contenido.split()

                for palabra in palabras:
                    palabra = palabra.upper()

                    if palabra.startswith("HK"):

                        if palabra in matriculas_hk:
                            matriculas_hk[palabra] += 1

                        else:
                            matriculas_hk[palabra] = 1
                
                for matricula in matriculas_hk:

                    print(matricula, ":", matriculas_hk[matricula])
                
            elif textos == 6:
                frecuencia = {}

                palabras = contenido.split()

                for palabra in palabras:
                    palabra = palabra.lower()

                    if palabra in frecuencia:
                        frecuencia[palabra] += 1

                    else:
                        frecuencia[palabra] = 1
                
                palabras_top = []
                cantidades_top = []

                for i in range(10):
                    palabra_mas_repetida = max(frecuencia, key = frecuencia.get)
                    cantidad = frecuencia[palabra_mas_repetida]
                    palabras_top.append(palabra_mas_repetida)
                    cantidades_top.append(cantidad)
                    del frecuencia[palabra_mas_repetida]

                plt.barh(palabras_top, cantidades_top)
                plt.xlabel("Frecuencia")
                plt.ylabel("Palabras")
                plt.title("Top 10 palabras más repetidas")
                plt.show()

            elif textos == 7:
                lineas = contenido.splitlines()

                longitudes = []

                for linea in lineas:
                    cantidad_caracteres = len(linea)
                    longitudes.append(cantidad_caracteres)
                
                plt.hist(longitudes, bins = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
                plt.xlabel("Cantidad de caracteres por línea")
                plt.ylabel("cantidad de lineas")
                plt.title("Histograma de longitud de lineas")
                plt.show()

            elif textos == 8:
                break
        
        # Opción 3
    
    elif opcion == 3:
        ruta = Path("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Reto\\Data\\EOH")
        datasets = list(ruta.glob("*.csv"))

        if datasets:
            print("\nDatasets disponibles:")

            contador = 1

            for archivo in datasets:
                print(f"{contador}) {archivo.name}")
                contador += 1
            
            seleccion = int(input("\nSeleccione un dataset: "))

            datasets_seleccionado = datasets[seleccion -1]

            print("\nDataset seleccionado:")
            print(datasets_seleccionado.name)
        
        else:
            print("\nNo se encontraron datasets CSV")

        while True:
            print("\n¿Que deseas hacer con el texto")
            print("1) Vista previa primeras díez filas")
            print("2) Vista previa ultimas cinco filas")
            print("3) Estadisticas Descriptivas")
            print("4) Gráfico Evolución temporal")
            print("5) Gráfico Comparación categorica")
            print("6) Gráfico y analisis correlación de variables")
            print("7) Volver al menú principal")

            opcion_csv = int(input("\nSelecciona la opcion: "))

            with open(datasets_seleccionado, "r", encoding="utf-8") as archivo:
                lector = csv.reader(archivo) 
                filas = list(lector)

            if opcion_csv == 1:
                print("\nPrimeras 10 filas")

                for fila in filas[:10]:
                    print(fila)

            elif opcion_csv == 2:
                print("\nUltimas 5 filas")

                for fila in filas[-5:]:
                    print(fila)
                
            elif opcion_csv == 3:
                encabezados = filas[0]
                columnas_numericas = []

                for columna in range(len(encabezados)):
                    es_numerica = True

                    for fila in filas[1:]:

                        try:
                            valor = fila[columna]
                            if valor != "":
                                float(valor)
                        except:
                            es_numerica = False
                            break

                    if es_numerica:
                        columnas_numericas.append(encabezados[columna])
                print("\nColumnas númericas disponibles: ")
                contador = 1

                for columna in columnas_numericas:
                    print(f"{contador}) {columna}")
                    contador += 1
                
                seleccion_columna = int(input("\nSeleccione una columna: "))
                nombre_columna = columnas_numericas[seleccion_columna - 1]
                indice_columna = encabezados.index(nombre_columna)

                datos_numericos = []

                for fila in filas[1:]:
                    valor = fila[indice_columna]

                    if valor != "":
                        datos_numericos.append(float(valor))
                
                total = len(datos_numericos)
                promedio = sum(datos_numericos)/total
                datos_ordenados = sorted(datos_numericos)
                mitad = total // 2
                mediana = datos_ordenados[mitad]
                maximo = max(datos_numericos)
                minimo = min(datos_numericos)

                print("Columna seleccionada:", nombre_columna)
                print("Total de registros válidos:", total)
                print("Promedio:", promedio)
                print("Mediana:", mediana)
                print("Valor máximo:", maximo)
                print("Valor mínimo:", minimo)

            elif opcion_csv == 4:
                encabezados = filas[0]
                print("\nColumnas disponibles: ")

                contador = 1

                for columna in encabezados:
                    print(f"{contador}) {columna}")
                    contador += 1

                seleccion_x = int(input("\nSeleccione la primera columna: "))
                seleccion_y = int(input("Seleccione la segunda columna: "))

                indice_x = seleccion_x - 1
                indice_y = seleccion_y - 1
                datos_x = []
                datos_y = []

                for fila in filas[1:]:
                    valor_x = fila[indice_x]
                    valor_y = fila[indice_y]

                    if valor_y != "":
                        try:
                            valor_y = float(valor_y)
                            datos_x.append(valor_x)
                            datos_y.append(valor_y)
                        except:
                            print("Dato invalido", valor_y)
                    
                plt.plot(datos_x, datos_y)
                plt.xlabel(encabezados[indice_x])
                plt.ylabel(encabezados[indice_y])
                plt.title("Evolución temporal")
                plt.xticks(rotation = 45)
                plt.show()

            elif opcion_csv == 5:
                encabezados = filas[0]
                print("\nColumnas disponibles:")
                contador = 1

                for columna in encabezados:
                    print(f"{contador}) {columna}")
                    contador += 1

                seleccion = int(input("\nSeleccione una columna categórica: "))
                indice = seleccion - 1

                frecuencia = {}

                for fila in filas[1:]:
                    categoria = fila[indice]

                    if categoria in frecuencia:
                        frecuencia[categoria] += 1

                    else:
                        frecuencia[categoria] = 1

                categorias = []
                cantidades = []

                for categoria in frecuencia:
                    categorias.append(categoria)
                    cantidades.append(frecuencia[categoria])

                plt.pie(cantidades, labels=categorias, autopct="%1.1f%%")
                plt.title("Comparación categórica")
                plt.show()

            elif opcion_csv == 6:
                encabezados = filas[0]
                columnas_numericas = []

                for columna in range(len(encabezados)):
                    es_numerica = True
                    
                    for fila in filas[1:]:
                        try:
                            valor = fila[columna]
                            if valor != "":
                                float(valor)
                        except:
                            es_numerica = False
                            break
                    
                    if es_numerica:
                        columnas_numericas.append(encabezados[columna])
                
                print("\nColumnas numéricas disponibles: ")
                contador = 1

                for columna in columnas_numericas:
                    print(f"{contador}) {columna}")
                    contador +=1
                
                seleccion_x = int(input("\nSeleccione la columna X: "))
                seleccion_y = int(input("Seleccione la columna Y: "))
                nombre_x = columnas_numericas[seleccion_x - 1]
                nombre_y = columnas_numericas[seleccion_y - 1]
                indice_x = encabezados.index(nombre_x)
                indice_y = encabezados.index(nombre_y)
                datos_x = []
                datos_y = []

                for fila in filas[1:]:
                    try:
                        valor_x = fila[indice_x]
                        valor_y = fila[indice_y]

                        if valor_x != "" and valor_y != "":
                            datos_x.append(float(valor_x))
                            datos_y.append(float(valor_y))
                    except:
                        pass
                
                plt.scatter(datos_x, datos_y)
                plt.xlabel(nombre_x)
                plt.ylabel(nombre_y)
                plt.title("Correlación de variables")
                plt.show()

            elif opcion_csv == 7:
                break

    elif opcion == 4:
        print("\nSaliendo del sistema...")
        break
    
    else:
        print("\nERROR: Opción inválida")
