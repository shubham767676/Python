name=input("\n Enter the name: ")
if len(name)>=3:        #Defining the minimum length
    print('\n Hello', name, end=", How are you? ") 
else:
    print("Enter minimum 3 characters")