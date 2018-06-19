                                      # ASSIGNMENT-8
              #Let’s lookout some interesting methods and properties of the commonly used packages.

#Q.1- What is Time Tuple?
#Ans-

#import  time
#print(time.gmtime())

#Q.2- Write a program to get formatted time.
#Ans-
#print(time.asctime())

# Q.3- Extract month from the time.
#Ans-
#import datetime
#d = datetime.date.today()
#print(d)
#print(d.month)

#Q.4- Extract day from the time.
#Ans-
# l=[]
# import time
# l=list(time.localtime())
# print(l[2])

#  Q.5- Extract date (ex : 11 in 11/01/2021) from the time.
# Ans-
#  import datetime
#  d=datetime.date.today()
#  print(d)
# print(d.day)

#Q.6- Write a program to print time using localtime
        # method.
#Ans-
#import time
#print(time.localtime())

#Q.7- Find the factorial of a number input by user using
    # math package functions.
#Ans-
#import math
#print(math.factorial(5))

#Q.8- Find the GCD of a number input by user using
    #  math package functions.
#Ans-
# import math
# a=int(input("Enter the value of A-"))
# b=int(input("Enter the value of B-"))
# print(math.gcd(a,b))

# Q.9- Use OS package and do the following tasks:
# 1. Get current working directory.
# 2. Get the user environment.
#Ans-
# import os
# print(os.getcwd())
# print(os.environ)
