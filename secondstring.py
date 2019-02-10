# Write a program that takes a user input string and outputs every second word.

text = str (input ('Please enter a sentence: ')) 
list = text.split(' ') # split() function allow us to separate each word and store it to list

l_list = len(list) # we check lenght of list 

i = 0
while i <= l_list:
    try: # we were getting an error, when list length was even. To avoid that I used TRY EXCEPT statement
        print (list[i], end = " ") # by using argument we can print in same line
    except IndexError:
        pass # skip error message when list length is even
    
    i = i + 2 # increment by 2 to skip every second word

print ('\n \n Thank You for using my program') 
