# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:33:09 2020

@author: littl
"""

products = []
while True: 
    name = input("Please enter product's name: ")
    if name == "q":   # quit 
        break
    price = input("Please enter the price: ")
    products.append([name, price])
print(products)



for p in products: 
    print(p[0], "'s price is", p[1])