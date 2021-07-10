# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 30 10:59:18 2021

# @author: ROHAN
# """

# FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:

# Coffee

# Espresso Coffee
# Cappuccino Coffee
# Latte Coffee
# Tea

# Plain Tea
# Assam Tea
# Ginger Tea
# Cardamom Tea
# Masala Tea
# Lemon Tea
# Green Tea
# Organic Darjeeling Tea
# Soups

# Hot and Sour Soup
# Veg Corn Soup
# Tomato Soup
# Spicy Tomato Soup
# Beverages

# Hot Chocolate Drink
# Badam Drink
# Badam-Pista Drink
# Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):

# Welcome to CCD

# Enjoy your

# Example 1:

# Input:
# c
# 1
# Output
# Welcome to CCD!
# Enjoy your Espresso Coffee!
# Example 2:

# Input
# t
# 9
# Output
# INVALID OUTPUT!

a=input()
n=int(input())
mainu=[["Espresso Coffee","Cappuccino Coffee","Latte Coffee"],["Plain Tea","Assam Tea","Ginger Tea","Cardamom Tea","Masala Tea","Lemon Tea","Green Tea","Organic Darjeeling Tea"],["Hot and Sour Soup","Veg Corn Soup","Tomato Soup","Spicy Tomato Soup",],["Hot Chocolate Drink","Badam Drink","Badam-Pista Drink"]]
if a=="C" or a=="c":
    if 0<n<4:
       print(f" Welcome to CCD!\nEnjoy your {mainu[0][n-1]}")
    else:
       print("INVALID OUTPUT!")
elif a=="t" or a=="T":
    if 0<n<9:
       print(f" Welcome to CCD!\nEnjoy your {mainu[1][n-1]}")
    else:
       print("INVALID OUTPUT!")
elif a=="S" or a=="s":
    if 0<n<5:
       print(f" Welcome to CCD!\nEnjoy your {mainu[2][n-1]}")
    else:
       print("INVALID OUTPUT!")
elif a=="B" or a=="b":
    if 0<n<3:
       print(f" Welcome to CCD!\nEnjoy your {mainu[3][n-1]}")
    else:
       print("INVALID OUTPUT!")
else:
    print("INVALID OUTPUT!")
