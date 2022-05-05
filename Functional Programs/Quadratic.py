'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

import cmath
def Quadratic(a,b,c):
    
    
        delta= (b*b)-(4*a*c)
        root1=(-b + cmath.sqrt(delta))/(2*a)
        root2=(-b - cmath.sqrt(delta))/(2*a)

        
        print(root1)
        print(root2)

try:
    a=int(input('Enter value of a: '))
    b=int(input('Enter value of b: '))
    c=int(input('Enter value of c: '))
    Quadratic(a,b,c)
    
except Exception as e:
    print("Invalid input", e)