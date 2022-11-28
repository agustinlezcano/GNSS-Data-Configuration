# coding=utf-8

import os
import re

'''
Funcion hecha para recibir el documento de input y de ahí pasarlo a BNC. El documento de entrada es BNC_input.txt
La info de cada estación está en una linea del archivo
'''
c = os.path.dirname(__file__)
zen = os.path.join(c,"BNC_input.txt")

stations = list()


with open(zen) as f:
    data = f.readline()
    while data:
        info = data.split(";")  #divido la linea y la convierto en una lista
        info[3] = info[3].replace(" ","_")
        #USER: escribir usuario de RAMSAC en IGN
        out = "//USER@ntrip.ign.gob.ar:2101/"+info[1]+" "+info[3]+" "+info[8]+" "+info[9]+" "+info[10]+" no 1, \n"   #Ver si lleva espacio entre estaciones
        stations.append(out)
        data = f.readline()

mountPoints = "mountPoints="+''.join(stations)
mountPoints = mountPoints.rstrip(' ,')
#print(mountPoints)
#print(type(mountPoints))


RinexObs = os.path.join(c,"PruebaRinexObs.bnc")

with open(RinexObs, 'r') as file:
    # read a list of lines into data
    dataRinex = file.readlines()
dataRinex[23] = mountPoints

with open(RinexObs, 'w') as file:
    file.writelines( dataRinex )    
    print(file)

