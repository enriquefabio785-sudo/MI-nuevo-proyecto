import matplotlib.pyplot as plt
import json
import biblioteca_proyecto as bl
with open("E:/universidad/proyecto CD NO TOCAR/data/salarios medios.json","r",encoding="utf-8") as f:
         salarios_medios=json.load(f)["salario por provincia"]
         

productos_basicos = ["cafe 284g", "arroz 1kg","frijoles negros 500g","frijoles colorados 500g","azucar blanca 1kg"]
cantidad = [bl.cantidad_por_salario("cafe"),bl.cantidad_por_salario("arroz"),bl.cantidad_por_salario("frijoles negros"),bl.cantidad_por_salario("frijoles colorados"),bl.cantidad_por_salario("azucar blanca")]

plt.figure(figsize=(8, 5))
plt.plot(productos_basicos, cantidad, marker='o', color='red', linewidth=2)
plt.title('Analisis de obtencion de la canasta basica')
plt.xlabel('alimentos basicos')
plt.ylabel('cantidad que se puede obtener')

plt.show()