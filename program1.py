# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun 28 08:29:13 2021

# @author: ROHAN
# """

# Find the nth term of the series.

# 1,1,2,3,4,9,8,27,16,81,32,243,…

def nth_term(n):
    a=1
    if n==1:
        print(1,end=" ")
    else:
        print(1,1,end=" ")
        for i in range(1,n-1):
            if i%2!=0:
               print(i*2,end=" ")
            else:
               print(i*3,end=" ")
        print()
n=int(input())
nth_term(n)
