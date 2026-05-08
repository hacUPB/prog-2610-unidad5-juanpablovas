# Explorador CLI Información de Vuelos Aeropuerto Holaya Herrera (EOH)

![Imagen](./Imagenes/ATR.jpg)

El explorador estará basado en la información de vuelos del Aeropuerto Olaya Herrera, en Medellín. Los datos incluirán tanto las salidas como las llegadas de vuelos, mostrando información como la aerolínea, número de vuelo, fecha y hora, destino, estado del vuelo y puerta de embarque.

- Los datos sera tomadas de la página oficial del aeropuerto (EOH):
https://www.aeropuertomedellin.co/salidas-y-llegadas

## Desarrollo del programa
El programa contará con un menú principal donde el usuario(operario) podrá usar cualquiera de la opciones que le apareceran en pantalla. Estas opciones seran:

    Opciones:
        1. Explorador de directorio
        2. Procesar bitacoras / textos (.txt)
        3. Analizar dataset de archivos abiertos (.csv)
        4. Fin

El menú se desarrollará más adelante.

Los csv los quiero hacer con datos y tablas de excel (pensando si crear el csv o buscarlo)

### Menú

### Explorador de directorio
En primer lugar, se inicia solicitando al usuario una ruta donde se encuentran almacenados los archivos del sistema. Se le muestra la ruta donde están los archivos y el usuario debe seleccionar la ruta.

El programa analiza si la ruta existe
- Si la ruta no existe se le imprimara un mensaje al usuario indicando que la dirrecion es incorrecta, y le solicitara nuevamente que ingrese la ruta o que vuelva al menu principal
- Si la ruta existe se accedera al contenido de la carpetra, se le listará al usuario los archivos. 

Cuando se tengan listados los archivos, el usuario podrá elegir el archivo para conocer una corta descripción del archivo. 

![Idea de explorador de directorio](./Imagenes/DiagramaReto_explorador.jpg)




