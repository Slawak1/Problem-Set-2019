# Problem No. 7 
# Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

# import moudules 'numpy','math' and 'cmath', from we can get functions sqrt(), around() 
# cmath will allow us to work in complex numbers in case of negative number provided
import numpy as np
import math as mt
import cmath as cm
import sys

# get number from user 
try:
    number = float (input ('Please enter number: ')) 
except ValueError:
    print ('Incorrect data, provided is not a number, start program and try again.')
    sys.exit()

if number < 0: # if negative number provided we need to transform negative real number to complex number (a+bj),  
    #c_number - complex number 
    c_number = cm.sqrt(complex(number,0))
    print(c_number)
    #r_number - rounded number
    r_number = np.around(c_number, decimals=1 )
    print ('Approximitation of squared number is ', r_number, ' This is a complex number')

else:
    number = mt.sqrt(number)
    print ('\n Square root of provided number is', number)

    #r_number - rounded number
    r_number = np.around(number, decimals=1 )
    print ('Approximitation of squared number is', r_number)


print ('\n Thank You for using my program!!')