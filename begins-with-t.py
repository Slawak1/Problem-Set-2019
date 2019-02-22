# Slawomir Sowa 
# Date: 03.02.2019
# Problem No. 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.


import datetime # import datetime module which contain datetime.now() function
day = datetime.datetime.now() # import current date and time to variable 'day'
a_str = day.strftime("%A") # string format with directive %A prints full weekday name, we save it as a string 'a_str'.
print ("Today is %s " % (a_str))


if a_str[0] == str('T'): # if first item in string (with index 0) is the same as a letter T IF block is executed 
    print ("Yes - %s begins with a letter \'T\'" % (a_str)) # if statement is true, this block is executed 
else:
    print ("No - %s does not begin with a \'T\'" % (a_str)) # if statement is false, this block is executed 

print ('\nThank You for using My program')