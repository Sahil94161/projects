# Q.1- Name and handle the exception occured in the following program:
#
# a=3
# if a<4:
#     a=a/(a-3)
#     print(a)
#Ans-
#ZeroDivisionError: division by zero
# try:
#     a = 3
#     if a < 4:
#         a = a / (a - 3)
#         print(a)
# except Exception:
#     print("Expection occur")


#Q.2- Name and handle the exception occurred in the following program:
# l=[1,2,3]
# print(l[3])
#Ans-
#IndexError: list index out of range
# try:
#     l=[123]
#     print(l[3])
# except Exception:
#      print("Expection occur")

#Q .3 - What will be the output of the following code:

# Program to depict Raising Exception

# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print("An exception")
#     raise  # To determine whether the exception was raised or not

#Ans-
# raise NameError("Hi there")  # Raise Error
# NameError: Hi there
# An exception

#Q.4- What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print ("a/b result in 0")
# 	else:
# 		print (c)

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
#Ans-
# -5.0
# a/b result in 0

#Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error
#Ans-
#import Error
# try:
#     import abcdf
#   #  print("import error")
# except Exception as e:
#     print(e)

# Value Error
#
# try:
#     z=int("abc")
# except Exception as e:
#     print(e)

#Index Error
# try:
#     l=[1,2,3]
#     print(l[8])
# except Exception as e:
#     print(e)

# Q.6- Create a user-defined exception AgeTooSmallError()
# that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate
# age number(less than 18).
#Ans-
# class AgeTooSmallError(Exception):
#     pass
#
# while True:
#     try:
#         age = int(input("Enter any of age:-"))
#         if(age<18):
#          raise AgeTooSmallError("age is less than 18")
#         break
#     except Exception as e:
#         print(e)
#
# print("age of above 18")