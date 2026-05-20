import matplotlib.pyplot as plt

# Datos
categorias = ['A320', 'B787', 'ATR 72', 'A350',"A380"]
valores = [10, 15, 20, 12, 30]

# Crear la gráfica de barras
# plt.bar(categorias, valores)
plt.barh(categorias, valores, color=['red', 'blue', 'green', 'orange'])

# Agregar título y etiquetas
plt.title('Horas de vuelo al día')
plt.xlabel('Aeronaves')
plt.ylabel('Horas')

# Mostrar la gráfica
plt.show()