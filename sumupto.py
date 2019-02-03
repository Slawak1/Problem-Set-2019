#Problem no 1. 
#Write a program that asks the user to input 
# any positive integer and outputs the
#sum of all numbers between one and that number.

import sys

a = int (input ("Enter a positive integer, Please: "))

# 'if' negative number statement will be printent. 
if a<0:
    print ("Sorry, but %d is a negative number." %(a))
    print ("Start program, and try again." )
    sys.exit(0) # will stop the program after negative number provided
else:
    print ("Your number is %d Thank You" %(a))


#declaration of variables
sum = 0
sum_total = 0

# While loop. loop will be repeted untill 'sum' is lower that 'a', every time added to 'sum_total'
while sum < a:
    
    sum = sum + 1
    sum_total = sum_total+sum

# print result 
print (sum_total)
print ("Sum of all numbers from 0 to %d is %d" %(a, sum_total))
print ("Thank You for calculations!!")