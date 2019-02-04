# Problem No. 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.


import datetime
day = datetime.datetime.now() # import current date and time 
a = day.strftime("%A") # string format with directive %A will print full weekday name.
print ("Today is %s " % (a))

#statement 'if' will check is first item on list 'a' same as letter T 
if a[0] == str('T'): 
    print ("Yes - %s  begins with a T" % (a))
else:
    print ("No - %s does not begin with a T" % (a))

