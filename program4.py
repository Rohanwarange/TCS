# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun 28 09:07:18 2021

# @author: ROHAN
# """

# Selection of MPCS exams include a fitness test which is conducted on ground. There will be a batch of 3 trainees, appearing for running test in track for 3 rounds. You need to record their oxygen level after every round. After trainee are finished with all rounds, calculate for each trainee his average oxygen level over the 3 rounds and select one with highest oxygen level as the most fit trainee. If more than one trainee attains the same highest average level, they all need to be selected.

# Display the most fit trainee (or trainees) and the highest average oxygen level.

# Note:

# The oxygen value entered should not be accepted if it is not in the range between 1 and 100.
# If the calculated maximum average oxygen value of trainees is below 70 then declare the trainees as unfit with meaningful message as “All trainees are unfit.
# Average Oxygen Values should be rounded.
# Example 1:

# INPUT VALUES
#             95

#             92

#             95

#             92

#             90

#             92

#             90

#             92

#             90

# OUTPUT VALUES
# Trainee Number : 1
# Trainee Number : 3
# Note:

# Input should be 9 integer values representing oxygen levels entered in order as

# Round 1

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Round 2

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Round 3

# Oxygen value of trainee 1
# Oxygen value of trainee 2
# Oxygen value of trainee 3
# Output must be in given format as in above example. For any wrong input final output should display “INVALID INPUT”

array=[[],[],[]]
for i in range(3):
    for j in range(3):
        array[i].append(list(map(int,input().split())))
a=array[0][0]+array[1][0]+array[2][0]
b=array[0][1]+array[1][1]+array[2][1]
c=array[0][2]+array[1][2]+array[2][2]
c=max(a,b,c)
if c==a:
    print(1)
elif c==b:
    print(2)
else:
    print(3)
