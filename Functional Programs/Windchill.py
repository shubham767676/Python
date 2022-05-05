'''
@Author: Shubham Singh
@Date: 05/05/2022
@Last Modified by: Shubham Singh
'''

def WindCalculation(t,v):
    try:
        # calculation part
        w=35.74+(0.6215*t)+((0.4275*t)-35.75)*pow(v,0.16)

        print('calculated windchill is: ')
        print(w)
    except Exception as e:
        print("invalid", e)    

def userinput():
         temp= int(input('Enter the value of temperature in Fahrenheit less then 50: '))
         vel= int(input('Enter wind speed in miles per hour from 3 to 120: '))
         return temp,vel

t,v = userinput()
if(v > 120 or v < 3 or t > 50 ):
    print("Can't get WindChill at this Parameters")
else:
    WindCalculation(t,v)