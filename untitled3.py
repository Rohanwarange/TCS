## -*- coding: utf-8 -*-
#"""
#Created on Fri Jul  2 08:49:41 2021
#
#@author: ROHAN
#"""
#
#
#Find the 15th term of the series?
#
#0,0,7,6,14,12,21,18, 28
#
#Explanation : In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }
#
# And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – }#
n=int(input())
if n%2==0:
    print(f"{n}th term of the series is {n//2*7}")
else:
    print(f"{n}th term of the series is {n//2*6}")
        