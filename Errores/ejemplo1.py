try: 
    valor = int(input("Ingrese un valor númerico: "))

except ValueError:
    print("El valor ingresado no es un número")

else:
    resultado = valor / 10
    print(f"Resultado es igual a {resultado}")

finally:
    print("Proceso ejecutado")
    




    