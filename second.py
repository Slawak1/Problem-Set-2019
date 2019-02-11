#  Problem No. 9
# Write a program that reads in a text file and outputs every second line. The program
# should take the filename from an argument on the command line.

# argv() is part of sys libreary.
import sys 

# validate file name, if empty or wrong file name error message will be printed. 
try:
    text = open (sys.argv[1]) # argv() is a list of arguments separated by space. 
except IndexError:
    print ("No file found. As an argument please use file name, example: python second.py yourfilename.txt")
    sys.exit()
except FileNotFoundError:
    print ("File not found. Check the name and try again.")    
    sys.exit()

#from input file lines are saved to list and list length is calculated.      
list = text.readlines()
l_list = len(list)

# to print every second line i can use FOR loop with step = 2.
i = 0
for i in range(0, l_list + 1, 2):
    try:
        print (list[i], end="\n")
    except IndexError:
        pass # skip error message when list length is even
        
print ("\n \n Thank You for using my program")