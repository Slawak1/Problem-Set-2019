# Problem No. 4
# Write a program that asks the user to input any positive integer and outputs the
# successive values of the following calculation. At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
# it by three and add one. Have the program end if the current value is one.

import sys # import system module

# Validation of user data inserted
# Try Except statement allow me to replace 'bad looking' error to defined text
try:
    number = int (input ("Enter a positive integer, Please: "))
except:
    print ('Provided is not a positive Integer. Start program and try again')
    sys.exit(0) # stops program after error

 
if number < 0: # check if number is negative
    # if negative number provided, statement is printend.
    print ("Sorry, but %d is a negative number." %(number))
    print ("Start program, and try again." )
    sys.exit(0) # will stop the program after negative number provided
else:
    print ("Your number is %d Thank You" %(number))

# while loop is repeated until number = 1 
while number != 1:
    if number%2 == 0: # IF statement checks is division remainder of number divided by 2 is equal 0 
        number = int (number/2) # if TRUE number is divided by 2 and printed 
        print (number, end=" ") # argument end=" " allow me to print in the same line
    else:
        number = int ((number * 3) + 1) #if not TRUE - number is multiplied by 3 and added 1 and printed 
        print (number, end=" ")

else: # if number equal 1 while loop ends, and statement is printed
    print ('\n \n Thank You for calculations') 