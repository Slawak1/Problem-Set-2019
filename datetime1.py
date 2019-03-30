# Problem No 8
# Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.

import datetime 


d = datetime.datetime.now() #get current date and time

# I used block of if, elif and else statements, to generate proper suffix depends on the day of the month 
if d.day in (1,21,31): # checks is todays day number in tuple 
    suffix = 'st'  # if True, assign proper suffix to variable and print 
    print (suffix)
elif d.day in (2,22):
    suffix = 'nd'
    print (suffix)
elif d.day in (3,23):
    suffix = 'rd'
    print (suffix)
else:
    suffix  = 'th'
    print (suffix)

print ((d.strftime('%A, %B %d'))+suffix, (d.strftime('%Y at %I:%M %p'))) #function strftime() - format string with directives as an arguments

print ("\n Thank You.")