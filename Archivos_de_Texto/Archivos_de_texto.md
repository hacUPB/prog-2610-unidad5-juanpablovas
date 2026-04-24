Un archivo es un conjunto ordenado de bytes, dependen del tipo de archivo los bytes representan una u otra cosa.

En un archivo de texto un byte representan caracteres

Para interactuar con un archivo se debe seguir:
    Apertura
    Lectura
    cierre
    manejo de errores.
-------
Si abro un archivo que no existe el programa lo crea.

# Tema 1
Si el archivo no existe con los modos w, se crea, pero si llevaba mas de la mitad, se borra todo lo que habia

diferencia entre R+ y W+ cuando un arrchivo no existe
    Crea un error si se hace con r y con w
    
Si intento abrir un archivo en modo lectura y no existe da error

Cuando abro una archivo es un objeto que contene:
    nombre de archivo, el modo en que fue abierto, la ubicacion del archivo, mas info

```python
    #Apertura o creacion de un archivo
    mi_archivo = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\saludo.txt","w")

    mi_archivo.write("Hola, mundo!")
    mi_archivo.close()
```

Experimento

```python
#Apertura o creacion de un archivo
mi_archivo = open("C:\\Users\\ESTUDIANTES\\Documents\\Programación_2026\\prog-2610-unidad5-juanpablovas\\Archivos_de_Texto\\saludo.txt","a")
#En la anterior linea se dió la dirección donde quiero guardar el archivo

x = 0
for i in range(5):
    x = x + 1
    mi_archivo.write(f"\n{x}")
    
mi_archivo.close()
