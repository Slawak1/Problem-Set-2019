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


while number != 1:
    if number%2 == 0:
        number = int (number/2)
        print (number)
    else:
        number = int ((number * 3) + 1)
        print (number)

else:
    print ('Thank You')