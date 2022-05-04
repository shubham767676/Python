'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

harmonic_range = int(input("Enter the range to Calculate Harmonic Number "))
harmonic_number = 0     #Defining initial Value

for i in range(1,harmonic_range+1):     #Harmonic Series= 1 1/2 1/3 1/4
    if harmonic_range == 0:     #Defining initial Value
        print("Enter Valid Range")

    else:
        harmonic_number += 1 / i
        print("The Harmonic NUmber is ",harmonic_number)
