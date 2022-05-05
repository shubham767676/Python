'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

import math
def Distance(a,b):
    
    distance= math.sqrt(pow(a,2)+pow(b,2))
    print(distance)

try:
    a=int(input('Enter the value of A: '))
    b=int(input('Enter the value of B: '))
    Distance(a,b)
except Exception as e:
    print("Invalid input",e)