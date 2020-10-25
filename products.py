# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:33:09 2020

@author: littl
"""
products = []

import os
#Check if the file is there
if os.path.isfile("products.csv"):
    print("Yeah! We found the file.")
    # To read the file
    with open("products.csv", "r") as f:
        for line in f:
            if"name, price" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    print(products)
else:
    print("Can't find the file....")

# To input the product name
while True: 
    name = input("Please enter product's name: ")
    if name == "q":   # quit 
        break
    price = input("Please enter the price: ")
    products.append([name, price])
print(products)

# To print the purchasing records
for p in products: 
    print(p[0], "'s price is", p[1])
    
# To write the file
with open ("products.csv", "w") as f:
        f.write("name, price\n")
        for p in products:
            f.write(p[0]+ ","+p[1]+"\n")
            
            