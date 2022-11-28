# coding=utf-8

import os
import re

def Historial_de_acciones(archivo):
    c = os.path.dirname(__file__)
    zen = os.path.join(c,archivo)
    lista_datos_accion= []
    f= open(zen,"r")                  
    for lista in f:  
        separador= lista.split(",")                                  
        lista_datos_accion.append(separador)                        
    return lista_datos_accion

###########_------------HACER FUNCION------------####################
#Con esta función abro un archivo .html, le saco los datos, borro parte de los datos innecesarios.
#Falta ingresar una tabla con los valores a verificar (ver trabajo TRUBI)
#Luego de ingresar la tabla, comparar y quedarse con la versión más nueva 
c = os.path.dirname(__file__)
zen = os.path.join(c,"estaciones.html")
print(zen)
with open(zen) as f:
    data = f.readlines()
print(data)

for i in data:   
    if "none" in i:
        print(i.index("none"))
        print("indice de none first: ", data.index(i))
        del(data[0:data.index(i)+1])
        break

print(data)

#Cargar Lista con versiones deseadas
log = Historial_de_acciones("Estaciones.csv")
print("log", log)

#Lista sin repetir (saco versiones viejas)
tick = ""
tickOld = ""
stations = []
for i in log:
    tick = i[0] +"-"+ i[1]
    print(tick)
    c = []
    for index, elem in enumerate(data):
        if tick in elem:
            c.append(index)    
            print(f"{tick} is found at index {index}")
            stations.append(data[data.index(elem)])
    print(c)
    tickOld = tick
print("New data: ", stations)
