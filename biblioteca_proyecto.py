import json
lista_de_productos=[]
diccionario={}
contador=1
lista=['plaz_1.json', 'plaz_2.json', 'plaz_3.json', 'plaz_4.json', 'plaz_5.json', 
 'plaz_6.json', 'plaz_7.json', 'plaz_8.json', 'plaz_9.json', 'plaz_10.json',
 'plaz_11.json', 'plaz_12.json', 'plaz_13.json', 'plaz_14.json', 'plaz_15.json',
 'plaz_16.json', 'plaz_17.json', 'plaz_18.json', 'plaz_19.json', 'plaz_20.json',
 'plaz_21.json', 'plaz_22.json', 'plaz_23.json',"plaz_24.json","plaz_25.json",
 "plaz_26.json","plaz_27.json","plaz_28.json","plaz_29.json","plaz_30.json"]
#creando una lista con todos los productos de las mipymes
for i in lista:
     with open(f"E:/universidad/proyecto CD NO TOCAR/data/mipymes/{i}","r",encoding="utf-8") as f:
         datos=json.load(f)
     lista_de_productos.extend(datos["productos"])
#creando diccionario de los productos por cada mipyme en un diccionario
for i in lista:
     with open(f"E:/universidad/proyecto CD NO TOCAR/data/mipymes/{i}","r",encoding="utf-8") as f:
         datos=json.load(f)
     diccionario[contador]=datos["productos"]
     contador+=1
#creando la variable salarios medios que es un diccionario con las provincias y sus salarios medios como valores
with open("E:/universidad/proyecto CD NO TOCAR/data/salarios medios.json","r",encoding="utf-8") as f:
         salarios_medios=json.load(f)["salario por provincia"]
#creando la variable precio actual del dolar que toma el ultimo valor del dolar por el Toque
with open("E:/universidad/proyecto CD NO TOCAR/data/precio_dolar.json","r",encoding="utf-8") as f:
         precio_actual_del_dolar_Cuba=json.load(f)["datos"][-1]["precio"]
#creando la variable paises con precios que es un diccionario con los mayores importadores de Cuba que tiene como valores otro diccionario que tiene los productos basicos y sus precios
with open("E:/universidad/proyecto CD NO TOCAR/data/costo de productos basicos en importadores.json","r",encoding="utf-8") as f:
         paises_con_precios=json.load(f)["precios de los paises con mas importaciones en Cuba"]
#funcion busqueda que devuelve una lista con los productos que coinciden ej:sal y galleta salada son coincidentes
def busqueda_coincidencias(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
    buscados=[]
    for x in lista_de_productos:
        if tipo is not None and tipo not in x["tipo"]:  
          continue
        if marca is not None and  marca not in x["marca"]:  
          continue
        if unidad is not None and  unidad not in x["unidad"]:  
          continue
        if pesaje is not None and x["pesaje"] != pesaje:  
          continue
        if precio is not None and x["precio"] != precio:  
          continue
        buscados.append(x)
    return buscados
#funcion busqueda que devuelve una lista con los precios productos que coinciden con la busqueda ej:sal y galleta salada son coincidentes
def busqueda_coincidencias_precios(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
    buscados=[]
    for x in lista_de_productos:
        if tipo is not None and tipo not in x["tipo"]:  
          continue
        if marca is not None and  marca not in x["marca"]:  
          continue
        if unidad is not None and  unidad not in x["unidad"]:  
          continue
        if pesaje is not None and x["pesaje"] != pesaje:  
          continue
        if precio is not None and x["precio"] != precio:  
          continue
        buscados.append(x["precio"])
    return buscados
#funcion busqueda que devuelve una lista con los productos que son exactamente iguales a la busqueda
def busqueda_exacta(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
    buscados=[]
    for x in lista_de_productos:
        if tipo is not None and tipo != x["tipo"]:  
          continue
        if marca is not None and  marca != x["marca"]:  
          continue
        if unidad is not None and  unidad != x["unidad"]:  
          continue
        if pesaje is not None and x["pesaje"] != pesaje:  
          continue
        if precio is not None and x["precio"] != precio:  
          continue
        buscados.append(x)
    return buscados
#funcion busqueda que devuelve una lista con los precios de los productos que son exactamente iguales a la busqueda
def busqueda_exacta_precios(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
    buscados=[]
    for x in lista_de_productos:
        if tipo is not None and tipo != x["tipo"]:  
          continue
        if marca is not None and  marca != x["marca"]:  
          continue
        if unidad is not None and  unidad!= x["unidad"]:  
          continue
        if pesaje is not None and x["pesaje"] != pesaje:  
          continue
        if precio is not None and x["precio"] != precio:  
          continue
        buscados.append(x["precio"])
    return buscados

#funcion que devuelve las mypimes donde se encuentran disponibles el producto que introduzcas
def disponibilidad_coincidencia(tipo=None,marca=None):
  lista_disponibles=[]
  for x  in diccionario:
    for y in diccionario[x]:
        if tipo is not None and tipo not in y["tipo"]:
            continue
        if marca is not None and  marca not in y["marca"]:  
            continue
        lista_disponibles.append(x)
        break
  if len(lista_disponibles)==0:
    return "este producto no esta disponible enninguna mypime"
  return lista_disponibles,"estas son las mypimes con la  disponibilidad de ese producto"

def disponibilidad_exacta(tipo=None,marca=None):
  lista_disponibles=[]
  for x  in diccionario:
    for y in diccionario[x]:
        if tipo is not None and tipo != y["tipo"]:
            continue
        if marca is not None and  marca != y["marca"]:  
            continue
        lista_disponibles.append(x)
        break
  if len(lista_disponibles)==0:
    return "este producto no esta disponible enninguna mypime"
  return lista_disponibles,"estas son las mypimes con la  disponibilidad de ese producto"


#funcion para calcular promedio        
def prom(lista):
    if len(lista)==0:
        return "lista vacia"
    x=sum(lista)/len(lista)
    return round(x,1)

#funcion que dado un peso , un precio y una unidad te da el precio unitario ej:peso=500 precio=1000 unidad=10 , el precio cada 10 gramos  es 20cup
def price_than_(peso=None,precio=None,unidad=None):
    if peso=="none" or precio=="none":
        return "tiene que colocar peso y precio"
    try:
            peso_num = float(peso)
            precio_num = float(precio)
            return round((precio_num / peso_num) * unidad, 1)
    except:
            return "los valores tienen que ser o deben poder ser llevados a int o float"
#funcion para calcular la mediana
def mediana(lista):
  lista=sorted(lista)
  if len(lista)%2!=0:
      return lista[len(lista)//2]
  return (lista[len(lista)//2]+lista[len(lista)//2-1])/2



#funcion que devuelve la cantidad de gramos o ml de un producto que se puede comprar con un salario medio en La Habana
def cantidad_por_salario(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
  precios=busqueda_exacta_precios(tipo,marca,unidad,pesaje,precio)
  return salarios_medios["La Habana"]/mediana(precios)

#funcion que devuelve la mediana de un producto buscado 
def mediana_producto(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
  precios=busqueda_exacta_precios(tipo,marca,unidad,pesaje,precio)
  return mediana(precios)

#funcion que devuelve la mediana de precio de un producto en dolares
def mediana_dolar(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
  precios=busqueda_exacta_precios(tipo,marca,unidad,pesaje,precio)
  return round(mediana(precios)/precio_actual_del_dolar_Cuba,2)

#evidencia de como crear una lista con las mipymes ordenadas de menor a mayor con la cantidad de productos que ofrecen
_=[]
mipymes_ordenadas_por_cantidad_de_productos=[]
contador=0
for i in lista:
     y=contador
     with open(f"E:/universidad/proyecto CD NO TOCAR/data/mipymes/{i}","r",encoding="utf-8") as f:
         datos=json.load(f)
     _.append([datos["ID"]])
     _[y].extend(datos["productos"])
     contador+=1
_.sort(key=len)
for x in _:
  mipymes_ordenadas_por_cantidad_de_productos.append(x[0])
  
#ya creada
mipymes_ordenadas_por_cantidad_de_productos=['018', '012', '003', '007', '021', '022', '028', '026', '023', '024', 
                                             '027', '009', '015', '011', '008', '017', '016', '001', '010', '019', 
                                             '025', '030', '029', '013', '004', '006', '014', '020', '005', '002']

#porciento respecto al precio en Cuba
def porciento(pais,producto):
 if producto =="harina 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("harina",None,None,1000)*100,1)
 if producto =="arroz 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("arroz",None,None,1000)*100,1)
 if producto =="azucar 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("azucar blanca",None,None,1000)*100,1)
 if producto =="sal 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("sal",None,None,1000)*100,1)
 if producto =="leche 1L":
   return round(paises_con_precios[pais][producto]/mediana_dolar("leche liquida",None,None,1000)*100,1)
 if producto =="12 huevos":
   return round(paises_con_precios[pais][producto]/(mediana_dolar("carton de huevos")/2.5)*100,1)
 if producto =="aceite 1L":
   return round(paises_con_precios[pais][producto]/mediana_dolar("aceite",None,None,1000)*100,1)
#diferencia de prociento respecto al precio en Cuba
def porciento_diferencia(pais,producto):
 if producto =="harina 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("harina",None,None,1000)*100-100,1)
 if producto =="arroz 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("arroz",None,None,1000)*100-100,1)
 if producto =="azucar 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("azucar blanca",None,None,1000)*100-100,1)
 if producto =="sal 1kg":
   return round(paises_con_precios[pais][producto]/mediana_dolar("sal",None,None,1000)*100-100,1)
 if producto =="leche 1L":
   return round(paises_con_precios[pais][producto]/mediana_dolar("leche liquida",None,None,1000)*100-100,1)
 if producto =="12 huevos":
   return round(paises_con_precios[pais][producto]/(mediana_dolar("carton de huevos")/2.5)*100-100,1)
 if producto =="aceite 1L":
   return round(paises_con_precios[pais][producto]/mediana_dolar("aceite",None,None,1000)*100-100,1) 
 







  










  

  
  





  




  

  
  
    
    
  
    

  







    
   

    
