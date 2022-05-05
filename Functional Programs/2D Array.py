'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

def PrintArray(R,C):
   
    a = []
    print("Enter the element:")
  
    
    for i in range(R):          
        b =[]
        for j in range(C):     
            b.append(input())
        a.append(b)
     
  
    for i in range(R):
        for j in range(C):
            print(a[i][j], end = " ")       #printing the array
        print()
         
try:
    PrintArray(3,3)
except Exception as e:
    print("invalid input",e)