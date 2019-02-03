#Problem no 1. 
#Write a program that asks the user to input 
# any positive integer and outputs the
#sum of all numbers between one and that number.

import sys

a = int (input ("Enter a positive integer, Please: "))
print (type(a))


if a<0:
    print ("C'mon, really? Do you know that %d is a negative number?" %(a))
    print ("Try again, You can do it.. " )
    sys.exit(0)
else:
    print ("Your number is %d Thank You" %(a,))



sum = 0
sum_total = 0
while sum < a:
    
    sum = sum + 1
    sum_total = sum_total+sum

print (sum_total)
print ("Sum of all numbers from 0 to %d is %d" %(a, sum_total))
print ("Yeah.. this is very good program")