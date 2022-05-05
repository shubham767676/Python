'''
Author: Shubham Singh
Date: 05/05/2022
Description: How many random numbers do you need to generate distinct coupon number?
'''

import random

No_Rand_numbers = int(input("Enter the number of distinct random numbers needed: "))

Rand_number = random.sample(range(0,pow(2,25)), No_Rand_numbers)
    

print(sorted(Rand_number))