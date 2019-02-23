# Slawomir Sowa 
# Date: 04.02.2019
# Problem No.3
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

 
for a in range (1000, 10000): # for loop iterate and repeatedly execute block if condition is TRUE   
    if a%6 == 0 and a%12 != 0: # Number is divided by 6 if remainder = 0 and is not divided by 12 if remainder != 0.
        print ("%a is divided by 6 but not divided by 12" %(a)) # if both conditions are "true" statemen is printed.
    
print ('\n \n Thank You for using My program')
