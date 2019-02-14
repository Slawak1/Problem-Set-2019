# Problem No 10
# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import matplotlib.pyplot as plt
import numpy as np


list_a = [] # list x
list_b = [] # list x**2
list_c = [] # list 2**x
i = 0

for i in range(0,4,1): # 

    list_a.append(i)
    b = i**2
    list_b.append(b)
    c = 2**i
    list_c.append(c)
   


print(list_a)
print(list_b)
print(list_c)

plt.plot(list_a, 'r',  list_b, 'g', list_c,'b' )

plt.show()







