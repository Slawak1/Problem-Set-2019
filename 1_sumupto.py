# Slawomir Sowa  21.02.2019
#Problem no 1. 
#Write a program that asks the user to input 
# any positive integer and outputs the
#sum of all numbers between one and that number.

import sys # import system module, which contain sys.exit() function

# First we check is provided number is Integer,
# Try Except statement allow me to replace 'bad looking' error to defined text
try:
    number = int (input ("Enter a positive integer, Please: ")) # int(input()) will allow user input only integer. Everything else return error
except:
    sys.exit('Provided is not a positive Integer. Start program and try again') # stops program and print message after error

# check if number is negative
if number < 0: 
    
    print ("Sorry, but %d is a negative number." %(number)) # strin formating operators %d, %s, %f (integer, string, float), I can use them to input variables into ptrinted string 
    sys.exit("Start program, and try again.") # will stop the program after negative number provided
else:
    print ("Your number is %d Thank You" %(number))


#declaration of variables
sum = 0
sum_total = 0

# Block in while loop will be repeted untill 'sum' is lower than 'number', every time added to 'sum_total'
while sum < number: 
    sum += 1 
    sum_total += sum

# print result 
# print (sum_total)
print ("Sum of all numbers from 0 to %d is %d" %(number, sum_total))
print ("\n \n Thank You for calculations!!")