# Slawomir Sowa 03.02.2019
# Problem No. 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.


import datetime # import datetime module which contain datetime.now() function
day = datetime.datetime.now() # import current date and time to variable 'day'
a_list = day.strftime("%A") # string format with directive %A will print full weekday name, we save it to variable 'a'.
print ("Today is %s " % (a_list))

#statement IF will check is first item on list 'a' same as letter T 
if a_list[0] == str('T'): 
    print ("Yes - %s begins with a letter \'T\'" % (a_list)) # if statement is true, this block will be executed 
else:
    print ("No - %s does not begin with a \'T\'" % (a_list)) # if statement is false, this block will be executed 

print ('\n \n Thank You for using My program')