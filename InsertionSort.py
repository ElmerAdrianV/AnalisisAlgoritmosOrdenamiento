# -*- coding: utf-8 -*-
"""
Created on Fri Sep 03 20:25:09 2021

@author: ElmerAdrianV
"""

def InsertionSort(input, length):
    for i in range(1,length-1):
        a=input[i]
        j=i
        while(0<j & a<input[j-1]):
            input[j]=input[j-1]
            j-=1
        input[j]=a

