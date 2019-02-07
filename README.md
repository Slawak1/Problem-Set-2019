# pands-problem-set

Problem Set 2019 for GMIT Data Analytics 

Technologies: Python

Launch Date: 03.02.2019

Author: Slawomir Sowa

Problem No.1 
    Write a program that asks the user to input any positive integer and outputs the
    sum of all numbers between one and that number.
Solution:
    To solve problem I used while loop,
    But before that I decide to verify provided by user number. I imported sys module which allow me to use methode exit() to stop program when needed. In case that user provide string I used Try and Except statement to change 'Bad looking Error' to delivered by me. When error ocured in Try block, Except block will be executed. In  Next step I checked is provided number positive or negative Integer. I used If Else Statement. If provided number lower than 0 program will stop with comment. I declared two variables.
    While loop every time checks is variable 'sum' lower than provided by user number. Every time variable 'sum' is incremented by 1. Also every time sum is added to sum_total. Program will end when condition sum < number is false. 

Problem No.2
    Write a program that outputs whether or not today is a day that begins with the
    letter T. An example of running this program on a Thursday is as follows.

Problem No.3
    Write a program that prints all numbers between 1,000 and 10,000 that are divisible
    by 6 but not 12.


