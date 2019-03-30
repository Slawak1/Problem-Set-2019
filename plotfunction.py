# Problem No 10
# Problem No. 9
# Slawomir Sowa 
# Date: 11.02.2019
# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.0,4.0,0.2) # NumPy arange() function returns evenly spaced numeric value with step 0.2                             

# functions calculated    
f1 = x
f2 = x**2 
f3 = 2**x 

# print (type(f1))

plt.plot(x,f1, 'r',x,f2, 'g', x,f3,'b' ) # plot chart, different colour of lines assigned to each function


# Setup chart
plt.title ('Chart x, $x^2$, $2^x$ in range (0,4)') # Title of chart 
plt.xlabel('X axis') # X axis and Y axis description
plt.ylabel('Y axis')
plt.legend(['f1 = x', 'f2 = $x^2$', 'f3 = $2^x$'], loc='upper left') # Legend of Chart
plt.grid (True) # shows grid on chart


plt.show() # shows chart window 






