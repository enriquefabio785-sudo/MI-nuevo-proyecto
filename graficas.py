import matplotlib.pyplot as plt
import json
import biblioteca_proyecto as bl
with open("E:/universidad/proyecto CD NO TOCAR/data/salarios medios.json","r",encoding="utf-8") as f:
         salarios_medios=json.load(f)["salario por provincia"]

#---------------------------------------------------------------------------Primer grafico---------------------------------------------------------------------------------------------
def primer_grafico():
      productos_basicos = ["aceite", "arroz","frijoles negros","sal","azucar blanca"]
      cantidad = [bl.cantidad_por_salario("aceite",None,None,1000),bl.cantidad_por_salario("arroz",None,None,1000),
            bl.cantidad_por_salario("frijoles negros",None,None,1000),bl.cantidad_por_salario("sal",None,None,1000),
            bl.cantidad_por_salario("azucar blanca",None,None,1000)]
      plt.figure(figsize=(20, 8),dpi=100,facecolor="lightgray")
      plt.plot(productos_basicos, cantidad, marker="o", color="red", linewidth=4)
      plt.bar(productos_basicos, cantidad,color=["yellow", "green", "black", "blue","white"],
             edgecolor='black',linewidth=3)
      plt.title("Analisis de obtencion de la canasta unitaria con el salario medio en La Habana",fontsize=15,color="Black",fontweight='bold',pad=10)
      plt.xlabel("Alimentos basicos 1 kilo/litro",fontsize=20,labelpad=15)
      plt.ylabel("Cantidad que se puede obtener",fontsize=20)
      return plt.show()

#---------------------------------------------------------------------------Segundo grafico---------------------------------------------------------------------------------------------
def segundo_grafico():
      productos_basicos = ["aceite 1L", "arroz 1kg","frijoles negros 1kg","sal 1kg","azucar blanca 1kg","refresco de pomo 1.5L","espaguetis 0.5kg","coditos 0.5kg","pasta de tomate 0.4kg"]
      cantidad= [bl.mediana_producto("aceite",None,None,1000),bl.mediana_producto("arroz",None,None,1000),bl.mediana_producto("frijoles negros",None,None,1000),
                 bl.mediana_producto("sal",None,None,1000),bl.mediana_producto("azucar blanca",None,None,1000),bl.mediana_producto("refresco de pomo",None,None,1500),
                 bl.mediana_producto("espaguetis",None,None,500),bl.mediana_producto("coditos",None,None,500),bl.mediana_producto("pasta de tomate",None,None,400)]
      plt.figure(figsize=(20,8), dpi=100,facecolor="#4c9297")
      plt.bar(productos_basicos,cantidad,color=["#ff3a3a","#ffa33a","#caff3a","#93ff3a",
                                                "#3affb3","#3ae8ff","#3a89ff","#b73aff","#ff3aad"])
      plt.axhline(y=salarios_medios["La Habana"],color="black",linestyle="--",linewidth=3, label="salario medio(La Habana)")
      plt.xlabel("Productos mas populares en las mipymes",fontsize=20,labelpad=15)
      plt.ylabel("Precio medio por producto",fontsize=20)
      plt.legend()
      return plt.show()


#---------------------------------------------------------------------------Tercer grafico---------------------------------------------------------------------------------------------
canasta_basica=["arroz 4kg","frijoles 1.5kg" ,"azucar 1kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 500gr","detergente en polvo 500gr","jabon(2)","pasta dental(1)"]
canasta_media=["arroz 5kg","frijoles 3kg" ,"azucar 2kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 1kg","detergente en polvo 1kg","jabon(2)","pasta dental(1)",
               "leche en polvo 1kg","harina 1kg","cafe molido 284gr","papel sanitario(4)"]
canasta_buena=["arroz 5kg","frijoles 3kg" ,"azucar 2kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 1kg","detergente en polvo 1kg","jabon(2)","pasta dental(1)",
               "leche en polvo 1kg","carton de huevos(1)","cafe molido 250-284gr","papel sanitario(4)","champu(1)"]
def tercer_grafico():
      canastas = ["canasta basica","canasta_media","canasta_buena"]
      precio= [bl.mediana_producto("arroz",None,None,1000)*4+bl.mediana_producto("frijoles negros",None,None,1000)*1.5+bl.mediana_producto("azucar blanca",None,None,1000)+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)+bl.mediana_producto("detergente en polvo",None,None,1000)//2+bl.mediana_producto("jabon")*2+
               bl.mediana_producto("pasta dental"),bl.mediana_producto("arroz",None,None,1000)*5+bl.mediana_producto("frijoles negros",None,None,1000)*3+bl.mediana_producto("azucar blanca",None,None,1000)*2+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)*2+bl.mediana_producto("detergente en polvo",None,None,1000)+bl.mediana_producto("jabon")*2+bl.mediana_producto("pasta dental")+
               bl.mediana_producto("leche en polvo",None,None,1000)+bl.mediana_producto("papel sanitario",None,None,4),bl.mediana_producto("arroz",None,None,1000)*5+bl.mediana_producto("frijoles negros",None,None,1000)*3+bl.mediana_producto("azucar blanca",None,None,1000)*2+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)*2+bl.mediana_producto("detergente en polvo",None,None,1000)+bl.mediana_producto("jabon")*2+bl.mediana_producto("pasta dental")+
               bl.mediana_producto("leche en polvo",None,None,1000)+bl.mediana_producto("papel sanitario",None,None,4)+bl.mediana_producto("carton de huevos")+bl.mediana_producto("cafe molido",None,None,284)+
               bl.mediana_producto("champu")]
      plt.figure(figsize=(20,8), dpi=100,facecolor="#19d0dd")
      plt.bar(canastas,precio,color=["#FF6B6B","#FFD93D","#6BCB77"])
      plt.axhline(y=salarios_medios["La Habana"],color="black",linestyle="--",linewidth=3, label="salario medio(La Habana)")
      plt.xlabel("Canastas establecidas",fontsize=20,labelpad=15)
      plt.ylabel("Precio de cada canasta",fontsize=20)
      plt.legend()
      return plt.show()

print(tercer_grafico())



    





