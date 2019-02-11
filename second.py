#  Problem No. 9
# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

import sys
text = open (sys.argv[1])

# print (text.read())

list = text.readlines()
l_list = len(list)
print (l_list)

i = 0
for i in range(0, l_list+1, 2):
    try:
        print (list[i], end="\n")
    except IndexError:
        pass # skip error message when list length is even
print ("\n \n Thank You for using my program")