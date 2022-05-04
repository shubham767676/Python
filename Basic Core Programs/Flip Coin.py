'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

import random

no_of_toss = int(input("Enter number of Coint Flips : "))
Heads = 0
Tails = 0

for value in range(no_of_toss):
    toss=random.random()
    if toss<0.5:
        print("Head")
        Tails += 1
    else:
        print("Tail")
        Heads +=1


Percentage_of_Heads = (Tails*100)/no_of_toss;       #Calculating the Percentage of Heads
Percentage_of_Tails = (Heads*100)/no_of_toss;       #Calculating the Percentage of Tails

print("Percentage of Heads is ",Percentage_of_Heads,"\nPercentage of Tails is ",Percentage_of_Tails)