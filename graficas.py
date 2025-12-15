import matplotlib.pyplot as plt
import json
import biblioteca_proyecto as bl
import numpy as np
with open("E:/universidad/proyecto CD NO TOCAR/data/salarios medios.json","r",encoding="utf-8") as f:
         salarios_medios=json.load(f)["salario por provincia"]
with open("E:/universidad/proyecto CD NO TOCAR/data/costo de productos basicos en EEUU.json","r",encoding="utf-8") as f:
         paises_con_precios=json.load(f)["precios de los paises con mas importaciones en Cuba"]

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
      plt.bar(productos_basicos,cantidad,color="#0d0a99")
      plt.title("Precios de productos populares en las mipymes",fontsize=20)
      plt.xlabel("Productos mas populares en las mipymes",fontsize=20,labelpad=15)
      plt.ylabel("Precio medio por producto(CUP)",fontsize=20)
      plt.legend()
      return plt.show()


#---------------------------------------------------------------------------Tercer grafico---------------------------------------------------------------------------------------------
canasta_basica=["arroz 5kg","frijoles 1.5kg" ,"azucar 1kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 1kg","detergente en polvo 500gr","jabon(2)","pasta dental(1)","10 huevos"]
canasta_media=["arroz 6kg","frijoles 3kg" ,"azucar 2kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 1kg","detergente en polvo 1kg","jabon(2)","pasta dental(1)",
               "leche en polvo 1kg","harina 1kg","cafe molido 284gr","papel sanitario(4)","20 huevos"]
canasta_buena=["arroz 7kg","frijoles 3kg" ,"azucar 2kg","aceite 1L","sal 0.5kg","pasta de tomate 400gr","espaguetis 1kg","detergente en polvo 1kg","jabon(2)","pasta dental(1)",
               "leche en polvo 1kg","carton de huevos(1)","cafe molido 250-284gr","papel sanitario(4)","champu(1)"]
def tercer_grafico():
      canastas = ["canasta basica","canasta_media","canasta_buena"]
      precio= [bl.mediana_producto("arroz",None,None,1000)*5+bl.mediana_producto("frijoles negros",None,None,1000)*1.5+bl.mediana_producto("azucar blanca",None,None,1000)+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)*2+bl.mediana_producto("detergente en polvo",None,None,1000)//2+bl.mediana_producto("jabon")*2+
               bl.mediana_producto("pasta dental")+bl.mediana_producto("carton de huevos")/3,bl.mediana_producto("arroz",None,None,1000)*6+bl.mediana_producto("frijoles negros",None,None,1000)*3+bl.mediana_producto("azucar blanca",None,None,1000)*2+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)*2+bl.mediana_producto("detergente en polvo",None,None,1000)+bl.mediana_producto("jabon")*2+bl.mediana_producto("pasta dental")+
               bl.mediana_producto("leche en polvo",None,None,1000)+bl.mediana_producto("papel sanitario",None,None,4)+bl.mediana_producto("carton de huevos")/1.5,bl.mediana_producto("arroz",None,None,1000)*7+bl.mediana_producto("frijoles negros",None,None,1000)*3+bl.mediana_producto("azucar blanca",None,None,1000)*2+
               bl.mediana_producto("aceite",None,None,1000)+bl.mediana_producto("sal",None,None,1000)//2+bl.mediana_producto("pasta de tomate",None,None,400)+
               bl.mediana_producto("espaguetis",None,None,500)*2+bl.mediana_producto("detergente en polvo",None,None,1000)+bl.mediana_producto("jabon")*2+bl.mediana_producto("pasta dental")+
               bl.mediana_producto("leche en polvo",None,None,1000)+bl.mediana_producto("papel sanitario",None,None,4)+bl.mediana_producto("carton de huevos")+bl.mediana_producto("cafe molido",None,None,284)+
               bl.mediana_producto("champu")]
      plt.figure(figsize=(20,8), dpi=100,facecolor="#19d0dd")
      plt.title("Precios de tipos de canasta en relacion al salario medio en La Habana",fontsize=20)
      plt.bar(canastas,precio,color=["#FF6B6B","#FFD93D","#6BCB77"])
      plt.axhline(y=salarios_medios["La Habana"],color="black",linestyle="--",linewidth=3, label="salario medio(La Habana)")
      plt.xlabel("Canastas establecidas para una persona",fontsize=20,labelpad=15)
      plt.ylabel("Precio de cada canasta(CUP)",fontsize=20)
      plt.legend(fontsize=14)
      return plt.show()
#---------------------------------------------------------------------------Cuarto grafico---------------------------------------------------------------------------------------------
def cuarto_grafico():
      productos=["harina 1kg","arroz 1kg","azucar 1kg","sal 1kg", "leche 1L","medio carton de huevos", "aceite 1L"]
      precios_Mexico=[paises_con_precios["Mexico"]["harina 1kg"],paises_con_precios["Mexico"]["arroz 1kg"],paises_con_precios["Mexico"]["azucar 1kg"],
                      paises_con_precios["Mexico"]["sal 1kg"],paises_con_precios["Mexico"]["leche 1L"],paises_con_precios["Mexico"]["medio carton de huevos"],
                      paises_con_precios["Mexico"]["aceite 1L"]]
      precios_España=[paises_con_precios["España"]["harina 1kg"],paises_con_precios["España"]["arroz 1kg"],paises_con_precios["España"]["azucar 1kg"],
                      paises_con_precios["España"]["sal 1kg"],paises_con_precios["España"]["leche 1L"],paises_con_precios["España"]["medio carton de huevos"],
                      paises_con_precios["España"]["aceite 1L"]]
      precios_Brasil=[paises_con_precios["Brasil"]["harina 1kg"],paises_con_precios["Brasil"]["arroz 1kg"],paises_con_precios["Brasil"]["azucar 1kg"],
                      paises_con_precios["Brasil"]["sal 1kg"],paises_con_precios["Brasil"]["leche 1L"],paises_con_precios["Brasil"]["medio carton de huevos"],
                      paises_con_precios["Brasil"]["aceite 1L"]]
      precios_China=[paises_con_precios["China"]["harina 1kg"],paises_con_precios["China"]["arroz 1kg"],paises_con_precios["China"]["azucar 1kg"],
                     paises_con_precios["China"]["sal 1kg"],paises_con_precios["China"]["leche 1L"],paises_con_precios["China"]["medio carton de huevos"],
                     paises_con_precios["China"]["aceite 1L"]]
      precios_Cuba=[bl.mediana_dolar("harina",None,None,1000),bl.mediana_dolar("arroz",None,None,1000),bl.mediana_dolar("azucar blanca",None,None,1000),bl.mediana_dolar("sal",None,None,1000),
                    bl.mediana_dolar("leche liquida",None,None,1000),bl.mediana_dolar("carton de huevos")/2,bl.mediana_dolar("aceite",None,None,1000)]
      n_productos = len(productos)
      posiciones = np.arange(n_productos) 
      ancho_barra = 0.15 
      plt.figure(figsize=(20,8), dpi=100,facecolor="#19d0dd")
      plt.barh(posiciones - 2*ancho_barra, precios_Mexico, ancho_barra, color="#6BFF90", label="México")
      plt.barh(posiciones - 1*ancho_barra, precios_España, ancho_barra, color="#CA1717", label="España")
      plt.barh(posiciones + 0*ancho_barra, precios_Brasil, ancho_barra, color="#2158AC", label="Brasil")
      plt.barh(posiciones + 1*ancho_barra, precios_China, ancho_barra, color="#AEB11C", label="China")
      plt.barh(posiciones + 2*ancho_barra, precios_Cuba, ancho_barra, color="#00D9FF", label="Cuba")
      plt.title("Precios de productos basicos(USD) en Cuba y sus mayores importadores",fontsize=20)
      plt.xlabel("Precios de los productos(USD)",fontsize=20,labelpad=15)
      plt.yticks( posiciones,productos, fontsize=14)
      plt.ylabel("Productos",fontsize=20)
      plt.legend(fontsize=14)
      return plt.show()
#---------------------------------------------------------------------------Quinto grafico---------------------------------------------------------------------------------------------
def quinto_grafico():
      productos=["harina 1kg","arroz 1kg","azucar 1kg","sal 1kg", "leche 1L","medio carton de huevos", "aceite 1L"]
      precios_Cuba=[bl.mediana_dolar("harina",None,None,1000),bl.mediana_dolar("arroz",None,None,1000),bl.mediana_dolar("azucar blanca",None,None,1000),bl.mediana_dolar("sal",None,None,1000),
                    bl.mediana_dolar("leche liquida",None,None,1000),bl.mediana_dolar("carton de huevos")/2,bl.mediana_dolar("aceite",None,None,1000)]
      porciento_Mexico=[f"{bl.porciento("Mexico","harina 1kg")}%",f"{bl.porciento("Mexico","arroz 1kg")}%",f"{bl.porciento("Mexico","azucar 1kg")}%",f"{bl.porciento("Mexico","sal 1kg")}%",
                        f"{bl.porciento("Mexico","leche 1L")}&",f"{bl.porciento("Mexico","medio carton de huevos")}%",f"{bl.porciento("Mexico","aceite 1L")}%"]
      precios_Mexico=[paises_con_precios["Mexico"]["harina 1kg"],paises_con_precios["Mexico"]["arroz 1kg"],paises_con_precios["Mexico"]["azucar 1kg"],
                      paises_con_precios["Mexico"]["sal 1kg"],paises_con_precios["Mexico"]["leche 1L"],paises_con_precios["Mexico"]["medio carton de huevos"],
                      paises_con_precios["Mexico"]["aceite 1L"]]
      plt.figure(figsize=(20,8), dpi=100,facecolor="#19d0dd")
      plt.plot(productos,precios_Cuba,color="#00D9FF",label="Cuba",marker="o",linestyle="none")
      plt.bar(porciento_Mexico,precios_Mexico,color="#6BFF90",label="Mexico")
      plt.title("Precios de los productos basicos de los importadores en relacion a Cuba",fontsize=20)
      plt.xlabel("Relacion de los productos de los importadores respecto a Cuba",fontsize=20,labelpad=15)
      plt.ylabel("Precios(USD)",fontsize=20)
      plt.legend(fontsize=14)
      return plt.show()

print(quinto_grafico())



    





