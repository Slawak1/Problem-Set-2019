# Problem No.3
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

a = 1000 #declaration of variable
while a<10000:  #loop will be repeated until condition is met 
    
    if a%6 == 0 and a%12 != 0: # we can use modulo operator % to check is number divided by 6, use logical operator "and" to check if is not divided by 12
        print ("%a is divided by 6 but not divided by 12" %(a)) # if both conditions are "true" statemen will be printed.
    a += 1  # increment operator
      
    
print ('Thank You for using My program')
