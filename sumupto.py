#Problem no 1. 
#Write a program that asks the user to input 
# any positive integer and outputs the
#sum of all numbers between one and that number.

import sys # import system module

# First we check is provided number is Integer,
# Try Except statement allow me to replace 'bad looking' error to defined text
try:
    number = int (input ("Enter a positive integer, Please: "))
except:
    print ('Provided is not a positive Integer. Start program and try again')
    sys.exit(0) # stop program after error

# check if number is negative
if number < 0: 
    
    print ("Sorry, but %d is a negative number." %(number))
    print ("Start program, and try again." )
    sys.exit(0) # will stop the program after negative number provided
else:
    print ("Your number is %d Thank You" %(number))


#declaration of variables
sum = 0
sum_total = 0

# While loop. loop will be repeted untill 'sum' is lower than 'a', every time added to 'sum_total'
while sum < number:
    
    sum = sum + 1
    sum_total = sum_total+sum

# print result 
print (sum_total)
print ("Sum of all numbers from 0 to %d is %d" %(number, sum_total))
print ("\n \n Thanks You for calculations!!")