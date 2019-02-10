# Problem No. 6
# Write a program that takes a user input string and outputs every second word.

text = str (input ('Please enter a sentence: ')) 
list = text.split(' ') # split() function allow us to separate each word and store it to list

l_list = len(list) # check lenght of list 

i = 0 

for i in range (0,l_list, 2):
    try: # I was getting an error, when list length was even. To avoid that I used TRY EXCEPT statement
        print (list[i], end = " ") # by using END argument statement can be printed in same line
    except IndexError:
        pass # skip error message when list length is even
    
    

print ('\n \n Thank You for using my program') 
