# Slawomir Sowa 
# Date: 9/02/2019
# Problem No. 6
# Write a program that takes a user input string and outputs every second word.

text = str (input ('Please enter a sentence: ')) # takes user input and save it to var text as a string.
a_list = text.split(' ') # split() function allow me to separate each word and store it to list

l_list = len(a_list) # checks length of list 

#i = 0 # define i as 0 to start iterate from index 0 on list

for i in range (0,l_list, 2):
    try: # I was getting an error, when list length was even. To avoid that I used TRY EXCEPT statement
        print (a_list[i], end = " ") # by using END argument I can print in the same line
    except IndexError:
        pass # skip error message when list length is even
    
print ('\n\nThank You for using my program') 
