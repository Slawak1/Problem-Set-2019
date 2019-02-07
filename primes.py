# Problem No. 5
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

import sys # import system module

# Try Except statement allow me to replace 'bad looking' error to defined text
try:
    number = int (input ("Enter a positive integer, Please: "))
except:
    print ('Provided is not a positive Integer. Start program and try again')
    sys.exit(0) # stop program after error

 
if number < 0: # check if number is negative
    # if negative number provided, statement will be printent.
    print ("Sorry, but %d is a negative number." %(number))
    print ("Start program, and try again." )
    sys.exit(0) # will stop the program after negative number provided
else:
    print ("Your number is %d Thank You" %(number))


list = [] # Empty list, i'll need it later 
i = 1 # counter 

while i <= number: 
    if number%i == 0: # statemen 'if' checks is number divided with remainder = 0   
        a = int (number/i) # if above is true, number is divided and added to list
        list.append(a) # if number is divided by 1 and by itself, list will contain only 2 elements. 
    i = i + 1    # incrementation 
    
print (list)
if len(list) == 2: # if list contain only 2 elements - provided number is prime 
    print ('Number %d is Prime' %(number))
else: # if list contain more than 2 elements is NOT prime
    print ('Number %d is NOT Prime' % (number))

print ('Thank You for using my Program')
