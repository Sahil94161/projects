#Q1. Create a threading process such that it sleeps for 5
# seconds and then prints out a message.
#Ans-
# import threading
# from  threading import Thread
# import time
# def display():
#     time.sleep(5)
#     print("Child Thread:",threading.current_thread().getName())
#
# t=Thread(target= display)
# t.setName("My thread")
# t.start()
#
# print("Main thread executing :",threading.current_thread())

#Q2. Make a thread that prints numbers from 1-10,
# waits for 1 sec between
#Ans-
# import threading
# from  threading import Thread
# import time
#
# def display(n):
#     for x in range(n):
#         time.sleep(1)
#         print(x)
# n=10
# t=Thread(target= display,args=(n,))
# t.start()


# Q3. Make a list that has 5 elements.Create a threading
# process that prints the 5 elements of the list with a
#  delay of multiple of 2 sec between each display.
# Delay goes like 2sec-4sec-6sec-8sec-10sec

#Ans-
# import threading
# from  threading import Thread
# import time
#
# def display():
#     u = 2
#     l=[1,2,3,4,5]
#     for x in l:
#         time.sleep(u)
#         print(x)
#         u = u+2
#
# t=Thread(target= display)
# t.start()

#Q4. Call factorial function using thread.
#Ans-
# import threading
# from  threading import Thread
# def fact(n):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     print(fac)
#
# n=int(input("Enter the value of factorial:-"))
# t=Thread(target=fact,args=(n,))
# t.start()