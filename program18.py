# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun 28 11:21:48 2021

# @author: ROHAN
# """

# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

# Take input as
# 1. Number of Interior walls
# 2. Number of Exterior walls
# 3. Surface Area of each Interior 4. Wall in units of square feet
# Surface Area of each Exterior Wall in units of square feet

# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

# Calculate and display the total cost of painting the property
# Example 1:

# 6
# 3
# 12.3
# 15.2
# 12.3
# 15.2
# 12.3
# 15.2
# 10.10
# 10.10
# 10.00
# Total estimated Cost : 1847.4 INR
int_wal=int(input())
ext_wal=int(input())
int_war=[]
ext_war=[]
for i in range(int_wal):
    int_war.append(float(input()))
for i in range(ext_wal):
s    ext_war.append(float(input()))
b=0
c=0
for i in int_war:
    a=18*i
    b+=a
for i in ext_war:
    d=12*i
    c+=d
print(f"Total estimated Cost : {b+c} INR")
