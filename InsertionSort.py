# -*- coding: utf-8 -*-
"""
Created on Fri Sep 03 20:25:09 2021

@author: ElmerAdrianV
"""
import random
from datetime import datetime # Fuente: https://docs.python.org/es/3/library/datetime.html

def insertion_sort(input, length):
    for i in range(1,length,1):
        a=input[i]
        j=i
        while(j>0 and a<input[j-1]):
            input[j]=input[j-1]
            j=j-1
        input[j]=a 
    return input;

x=[]
length=1000000
for i in range(0,length):
    x=x+[random.randint(0, length)]
print(x)

print("Tiempo inicio:")
print(datetime.now())

x=insertion_sort(x,length)

print("Tiempo final:")
print(datetime.now())

print(x)