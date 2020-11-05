# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:33:09 2020

@author: littl
"""

 # To read the file
def read_file(filename):
     products = []    
     with open(filename, "r") as f:
         for line in f:
             if"name, price" in line:
                 continue
             name, price = line.strip().split(",")
             products.append([name, price])
             return products

# 2. To input the product name
def user_input(products):
    while True: 
        name = input("Please enter product's name: ")
        if name == "q":   # quit 
            break 
        price = input("Please enter the price: ")
        products.append([name, price])
    print(products)
    return products
    
# 3. To print the purchasing records
def print_products(products):
    for p in products: 
        print(p[0], "'s price is", p[1])

# 4. To write the file
def write_file(filename, products):
    with open (filename, "w") as f:
            f.write("name, price\n")
            for p in products:
                f.write(p[0]+ ","+p[1]+"\n")

def main():
    import os
    filename = "products.csv"
    if os.path.isfile(filename):
        print("Yeah! We found the file.")
        products = read_file(filename)
    else:
        print("Can't find the file.")
    products = user_input(products)
    print_products(products)
    write_file("products.csv", products)


main()



 