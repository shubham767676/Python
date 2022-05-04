'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

Year=int(input("\n Enter the Year"))

if Year < 1000 or Year > 9999:
    print("Please enter 4 digit number")        #Ensuring 4 digit number

if (Year%4 ==0):     #used Logical Operation
    print("Leap Year")

else:
    print("Not a Leap Year")


















#(Year%100 == 0) and (Year%400 == 0) or
#if len(Year)>=4:

#elif (Year/4)
#    print("It's a Leap Year")
    
#    else:
#        print("Enter 4 digit number")