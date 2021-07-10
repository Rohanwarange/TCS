## -*- coding: utf-8 -*-
#"""
#Created on Fri Jul  2 09:54:07 2021
#
#@author: ROHAN
#"""
#
#
#Addition of two numbers a Twist
#1. Using a method, pass two variables and find the sum of two numbers.
#
#Test case:
#
#Number 1 – 20
#
#Number 2 – 20.38
#
#Sum = 40.38
#
#There were a total of 4 test cases. Once you compile 3 of them will be shown to you and 1 will be a hidden one. You have to display error message if numbers are not numeric.
#

try:
    a=int(input())
    b=int(input())
except ValueError:
    print("numeric Values only")
print(a+b)    

    