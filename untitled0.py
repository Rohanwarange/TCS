# -*- coding: utf-8 -*-
#"""
#Created on Fri Jul  2 08:11:58 2021
#
#@author: ROHAN
#"""
##Prime Numbers with a Twist
#Ques. Write a code to check whether no is prime or not. Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, And if yes pas no as a parameter to prime() and check whether no is prime or not?
#
#Whether the number is positive or not, if it is negative then print the message “please enter the positive number”
#It is positive then call the function prime and check whether the take positive number is prime or not.#

def prime(n):
    if n>1:
       for i in range(2,n//2):
           if n%i==0:
              print("enter the number is Not Prime : ”")
              break
    else:     
         print("enter the number is Prime : ”")
        
                
                
n=int(input())
if n<=0:
    print("“please enter the positive number”")
else:
    prime(n)
   
    