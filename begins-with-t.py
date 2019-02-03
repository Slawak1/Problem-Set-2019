# Problem No. 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T. An example of running this program on a Thursday is as follows.


import datetime
day = datetime.datetime.now()
a = day.strftime("%A")
print ("Today is %s " % (a))

if a[0] == str('T'):
    print ("Yes - %s  begins with a T" % (a))
else:
    print ("No - %s does not begin with a T" % (a))



