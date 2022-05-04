'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
@Title : User Input and Replace String Template
'''
name=input("\n Enter the name: ")
if len(name)>=3:        #Defining the minimum length
    print('\n Hello', name, end=", How are you? ") 
else:
    print("Enter minimum 3 characters")