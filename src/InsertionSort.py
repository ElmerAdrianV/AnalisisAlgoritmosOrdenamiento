# -*- coding: utf-8 -*-
"""
Created on Fri Sep 03 20:25:09 2021
@author: ElmerAdrianV
"""
import random
from datetime import datetime # Fuente: https://docs.python.org/es/3/library/datetime.html
import string                 #Fuente: https://pynative.com/python-generate-random-string/

def insertion_sort(lista):
    for i in range(1,len(lista),1):
        a=lista[i]
        j=i
        while(j>0 and a<lista[j-1]):
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=a 

#regresa los segundos que se tarda un algoritmo en ordenar una lista dada
def get_time(sortAlgorithm, unorderedlist):
    start=datetime.now()
    sortAlgorithm(unorderedlist)
    end=datetime.now()
    return (end.minute-start.minute)*60+(end.second-start.second)+(end.microsecond-start.microsecond)/1000000 

# obtiene un string de 4 caracteres al azar
def get_random_string4():
    randomString=''.join(random.choice(string.ascii_lowercase) for i in range(4))
    return randomString

#---------CUIDADO: ZONA DE PRUEBAS CON STRING-------------#

timesExpIS=[]
##timesExpSS=[]
##timesExpMSR=[]
##timesExpMSI=[]
length=16
for j in range(0,8):
    x=[]
    for i in range(0,length):
        x.append(get_random_string4())
    length*=2
    unorderedListIS=x.copy()   # copia para el insertion sort
    # unorderedListSS=x.copy()  # copia para el selection sort
    # unorderedListMSR=x.copy() # copia para el merge sort recursivo
    # unorderedListMSI=x.copy() # copia para el merge sort iterativo
    
    for i in range(0,10):
        timesExpIS.append(get_time(insertion_sort, unorderedListIS))
        # timesExpSS.append(get_time(selection_sort, unorderedListSS))
        # timesExpMSR.append(get_time(merge_sort_recursivo, unorderedListMSR))
        # timesExpMSI.append(get_time(merge_sort_iterativo, unorderedListMSI))
        
        unorderedListIS=x.copy()   # copia para el insertion sort
        # unorderedListSS=x.copy()  # copia para el selection sort
        # unorderedListMSR=x.copy() # copia para el merge sort recursivo
        # unorderedListMSI=x.copy() # copia para el merge sort iterativo

timesIS=[]
##timesSS=[]
##timesMSR=[]
##timesMSI=[]
for j in range(1,9):
    x=[]
    length=100*j
    for i in range(0,length):
        x.append(get_random_string4())
    
    unorderedListIS=x.copy()   # copia para el insertion sort
    # unorderedListSS=x.copy()  # copia para el selection sort
    # unorderedListMSR=x.copy() # copia para el merge sort recursivo
    # unorderedListMSI=x.copy() # copia para el merge sort iterativo
    
    for i in range(0,10):
        timesIS.append(get_time(insertion_sort, unorderedListIS))
        # timesSS.append(get_time(selection_sort, unorderedListSS))
        # timesMSR.append(get_time(merge_sort_recursivo, unorderedListMSR))
        # timesMSI.append(get_time(merge_sort_iterativo, unorderedListMSI))
        
        unorderedListIS=x.copy()   # copia para el insertion sort
        # unorderedListSS=x.copy()  # copia para el selection sort
        # unorderedListMSR=x.copy() # copia para el merge sort recursivo
        # unorderedListMSI=x.copy() # copia para el merge sort iterativo
'''
x=[]
for i in range(0,200):
    x=x+[200-i]
print(get_time(insertion_sort, x)) 

for i in range(0,length):
    x=x+[random.randint(0, length)]

print("Tiempo inicio:")
print(datetime.now())

x=insertion_sort(x)

print("Tiempo final:")
print(datetime.now())

# print(x)

'''