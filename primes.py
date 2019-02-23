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
    # if negative number provided, statement will be printend.
    print ("Sorry, but %d is a negative number." %(number))
    print ("Start program, and try again." )
    sys.exit(0) # will stop the program after negative number provided
else:
    print ("\n Your number is %d Thank You" %(number))


a_list = [] # create Empty list, i'll need it later 

for i in range (1, number+1): 
    if number%i == 0: # statemen 'if' checks is number divided with remainder = 0   
        a = int (number/i) # if above is true, number is divided and added to list
        a_list.append(a) # if number is divided by 1 and by itself, list contains only 2 elements. 
    
    
print ('%d is divided by ' %(number), a_list )
if len(a_list) == 2: # check list length, if list contain only 2 elements - provided number is prime 
    print ('Number %d is Prime' %(number))
else: # if list contain more than 2 elements number is NOT prime
    print ('Number %d is NOT Prime' % (number))

print ('\n \n Thank You for using my Program')
