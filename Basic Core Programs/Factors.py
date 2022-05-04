'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

num=int(input("Enter Integer Value: "))
i=2
Number=num
while Number > 1:
    if Number % 1==0 :
        print(i,end="\n")
        Number=int(Number/i)    
    else:
        i=i+1