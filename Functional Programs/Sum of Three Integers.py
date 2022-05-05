'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''
def sumofint(arr, n):
 
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             
    
    if (found == False):
        print("Not Exist")
 

arr = [0, -4, 3, -4, 1]
n = len(arr)
sumofint(arr, n)