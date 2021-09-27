# -*- coding: utf-8 -*-
"""
Created on Fri Sep 03 20:25:09 2021
@author: ElmerAdrianV
"""
import random
from datetime import datetime # Fuente: https://docs.python.org/es/3/library/datetime.html
import string                 #Fuente: https://pynative.com/python-generate-random-string/

#------class Algortimos_Ordenamiento:-----------#
def selection_sort(A):
    for i in range(len(A)):
        minimo=i;
        for j in range(i,len(A)):
            if(A[j] < A[minimo]):
                minimo=j
        if(minimo != i):
            aux=A[i]
            A[i]=A[minimo]
            A[minimo]=aux 

def insertion_sort(lista):
    for i in range(1,len(lista),1):
        a=lista[i]
        j=i
        while(j>0 and a<lista[j-1]):
            lista[j]=lista[j-1]
            j=j-1
        lista[j]=a 

##merge es el que realmente ordena, al ir checando los componentes        
def merge(izquierda, derecha):
    lista_ordenada =[]
    i=j=0
    
    while i < len(izquierda) and j < len(derecha):
        #compara los elementos en cada posicion de ambas listas
        if izquierda[i] < derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j +=1
            
    #los elemntos restantes son agregados al final de la lista
    #claro esta que solo 1 de izquierda o derecha tendra elementos que agregar
    lista_ordenada.extend(izquierda[i:])
    lista_ordenada.extend(derecha[j:])
    return lista_ordenada

def merge_sort_recursivo(lista):
    tam = len(lista)
    if(tam==1):
        return lista
    mitad = tam//2
    #Para asegurarnos de que todas las particiones sean descompuestas a sus componentes individuales, 
    #llamamos recursivamente a la funcion merge sort
    izquierda = merge_sort_recursivo(lista[:mitad])
    derecha = merge_sort_recursivo(lista[mitad:])
    #una vez descompuesto a la unidad, se empieza a unir por las llamadas en el Call Stack
    return merge(izquierda, derecha)

    
def merge_it(lista, aux, desde, medio, hasta):

    k = desde #para la auxiliar
    i = desde #para la original, primera mitad
    j = medio + 1 #para la original, segunda mitad

    # while hasta que no halla elementos ni en la izquierda ni en la derecha
    while i <= medio and j <= hasta:
        if lista[i] < lista[j]:
            aux[k] = lista[i]
            i += 1
        else:
            aux[k] = lista[j]
            j += 1

        k += 1

    #naturalmente, se cumplira una de las 2 condiciones.
    #por lo cual debemos de copiar los elementos restantes
    #aunque es obvio que no ocupamos copiar la otra mitad, porque ya estan ordenados en su posicion
    while i < len(lista) and i <= medio:
        aux[k] = lista[i]
        k += 1
        i += 1

    # Copiamos a la lista original para que, ahora si, este ordenado
    for i in range(desde, hasta + 1):
        lista[i] = aux[i]
        
def merge_sort_iterativo(lista):

    inicio = 0
    fin = len(lista) - 1

    # Ordena la lista usando una lista auxiliar
    aux = lista.copy()

    # divide la lista en bloques de tamaño 'm'
    # m = [1, 2, 4, 8, 16…]

    m = 1
    while m <= (fin - inicio): #ie, mientras podamos seguir haciendo subdivisiones

        # m = 1, i = [0, 2, 4, 6, 8…]
        # m = 2, i = [0, 4, 8, 12…]
        # m = 4, i = [0, 8, 16…]
        # …

        for i in range(inicio, fin, 2*m):
            desde = i
            medio = (i + m) - 1
            hasta = min( (i + 2*m - 1), fin) 
            #llegara el punto donde i+2*m superara a fin, en ese caso no podemos llamar a posiciones que no existen
            merge_it(lista, aux, desde, medio, hasta)

        m = 2*m


#-------class Funciones_Auxilares:----------#
    #regresa los segundos que se tarda un algoritmo en ordenar una lista dada
def get_time(sortAlgorithm, unorderedlist):
    start=datetime.now()
    sortAlgorithm(unorderedlist)
    end=datetime.now()
    return (end.minute-start.minute)*60 +(end.second-start.second) +(end.microsecond-start.microsecond)/1000000


# obtiene un string de 4 caracteres al azar
def get_random_string4():
    randomString=''.join(random.choice(string.ascii_lowercase) for i in range(4))
    return randomString

def pruebasString(sort,tipo, potencia): #(insertionSort, BC,1)
    tiempos=[]
    for j in range(1,11):
        if(potencia==1):
            length=2**(3+j) # [16,8096]
        else:
            length=100*j #[100-1000]
        lista=[]
        generaLista(lista,tipo, length)
        for i in range(0,10):
            listaDesordenada=lista.copy()   # copia para el ordenar
            tiempos.append(get_time(sort, listaDesordenada))
        lista.clear()
    return tiempos

def generaLista(lista,tipo, length):
    for i in range(length):
        lista.append( get_random_string4() )
    if(tipo!='AV'):
        lista.sort()
        if(tipo!='BC'):
            lista.reverse()

#---------CUIDADO: ZONA DE PRUEBAS CON STRING-------------#
"""
tiempos=pruebasString(insertion_sort, 'AV', 1)
print(tiempos)
tiempos=pruebasString(insertion_sort, 'BC', 1)
print(tiempos)
tiempos=pruebasString(insertion_sort, 'WC', 1)
print(tiempos)       


tiempos=pruebasString(insertion_sort, 'AV', 0)
print(tiempos)
tiempos=pruebasString(insertion_sort, 'BC', 0)
print(tiempos)
tiempos=pruebasString(insertion_sort, 'WC', 0)
print(tiempos) 

tiempos=pruebasString(selection_sort, 'AV', 1)
print(tiempos)
tiempos=pruebasString(selection_sort, 'BC', 1)
print(tiempos)
tiempos=pruebasString(selection_sort, 'WC', 1)
print(tiempos)       


tiempos=pruebasString(selection_sort, 'AV', 0)
print(tiempos)
tiempos=pruebasString(selection_sort, 'BC', 0)
print(tiempos)
tiempos=pruebasString(selection_sort, 'WC', 0)
print(tiempos)       

tiempos=pruebasString(merge_sort_recursivo, 'AV', 1)
print(tiempos)
tiempos=pruebasString(merge_sort_recursivo, 'BC', 1)
print(tiempos)
tiempos=pruebasString(merge_sort_recursivo, 'WC', 1)
print(tiempos)       

tiempos=pruebasString(merge_sort_recursivo, 'AV', 0)
print(tiempos)
tiempos=pruebasString(merge_sort_recursivo, 'BC', 0)
print(tiempos)
tiempos=pruebasString(merge_sort_recursivo, 'WC', 0)
print(tiempos)       

"""
tiempos=pruebasString(merge_sort_iterativo, 'AV', 1)
print(tiempos)
tiempos=pruebasString(merge_sort_iterativo, 'BC', 1)
print(tiempos)
tiempos=pruebasString(merge_sort_iterativo, 'WC', 1)
print(tiempos)

tiempos=pruebasString(merge_sort_iterativo, 'AV', 0)
print(tiempos)
tiempos=pruebasString(merge_sort_iterativo, 'BC', 0)
print(tiempos)
tiempos=pruebasString(merge_sort_iterativo, 'WC', 0)
print(tiempos)       
       
