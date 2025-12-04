import json
lista_de_productos=[]
lista=['plaz_1.json', 'plaz_2.json', 'plaz_3.json', 'plaz_4.json', 'plaz_5.json', 
 'plaz_6.json', 'plaz_7.json', 'plaz_8.json', 'plaz_9.json', 'plaz_10.json',
 'plaz_11.json', 'plaz_12.json', 'plaz_13.json', 'plaz_14.json', 'plaz_15.json',
 'plaz_16.json', 'plaz_17.json', 'plaz_18.json', 'plaz_19.json', 'plaz_20.json',
 'plaz_21.json', 'plaz_22.json', 'plaz_23.json']
for i in lista:
     with open(f"E:/universidad/proyecto CD NO TOCAR/data/mypimes/{i}","r",encoding="utf-8") as f:
         datos=json.load(f)
     lista_de_productos.extend(datos["productos"])

def busqueda(tipo=None,marca=None,unidad=None,pesaje=None,precio=None):
    buscados=[]
    for x in lista_de_productos:
        if tipo is not None and x["tipo"] != tipo:  
          continue
        if marca is not None and x["marca"] != marca:  
          continue
        if unidad is not None and x["unidad"] != unidad:  
          continue
        if pesaje is not None and x["pesaje"] != pesaje:  
          continue
        if precio is not None and x["precio"] != precio:  
          continue
        buscados.append(x)
    return buscados

        
def prom(lista):
    if len(lista)==0:
        return "lista vacia"
    x=sum(lista)/len(lista)
    return round(x,1)


def price_than_10gr(peso="none",precio="none"):
    if peso=="none" or precio=="none":
        return "tiene que colocar peso y precio"
    try:
            peso_num = float(peso)
            precio_num = float(precio)
            return round((precio_num / peso_num) * 10, 1)
    except:
            return "los valores tienen que ser o deben poder ser llevados a int o float"


    
   

    
