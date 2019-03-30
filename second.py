# Problem No. 9
# Slawomir Sowa 
# Date: 11.02.2019
# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

# argv() is part of sys library.
import sys 

# validate file name, if none or wrong file name provided, error message will be printed. 
try:
    text = open (sys.argv[1]) # argv() is a list of arguments separated by space and taken from command line. 
except IndexError:
    sys.exit("No file found. As an argument please use file name, example:$ python second.py yourfilename.txt")
except FileNotFoundError:   
    sys.exit("File not found. Check the name and try again.")

# print (type(text))
    
a_list = text.readlines() # To read lines from file I used readline() function, readline() return a list 
l_list = len(a_list) # also list length is calculated. 

# print (type(a_list)) - return list
# print (l_list) 

# to print every second line i used FOR loop with step = 2.
i = 0 
for i in range(0, l_list, 2):
    try:
        print (a_list[i], end="\n")
    except IndexError: # skip error message when list length is even
        pass 
        
print ("\n \n Thank You for using my program")