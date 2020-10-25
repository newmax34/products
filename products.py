# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:33:09 2020

@author: littl
"""

products = []
with open("products.csv", "r") as f:
    for line in f:
        if"name, price" in line:
            continue
        name, price = line.strip().split(",")
        products.append([name, price])
print(products)



while True: 
    name = input("Please enter product's name: ")
    if name == "q":   # quit 
        break
    price = input("Please enter the price: ")
    products.append([name, price])
print(products)



for p in products: 
    print(p[0], "'s price is", p[1])
    

with open ("products.csv", "w") as f:
        f.write("name, price\n")
        for p in products:
            f.write(p[0]+ ","+p[1]+"\n")
            
            