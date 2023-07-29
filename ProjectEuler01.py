# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:44:43 2023

@author: Jonas
"""

soma = 0

for numero in range(1000):
    if(numero % 3 == 0) or (numero % 5 == 0):
        soma += numero

print(soma)