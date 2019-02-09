# Problem No. 7 
# Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

import numpy as np
import math

number = float (input ('Please enter positive number: '))
number = math.sqrt(number)

print (number)

r_number = np.around(number, decimals=1 )

print (r_number)