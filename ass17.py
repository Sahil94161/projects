# Q1. Write a python program using tkinter interface to
# write Hello World and a exit button that closes the interface.
# Ans-
# from tkinter  import *
# import sys
# def exit():
#     sys.exit()
# w=Tk()
# l=Label(w,text="Hello World",width=50,bg="green",fg="red")
# l.pack()
# b=Button(w,text="Exit",width=25,bg="yellow",command=exit)
# b.pack()
# w.mainloop()

# Q2. Write a python program to in the same interface as above
# # and create a action when the button is click it will display
# # some text.
#Ans-
# from tkinter  import *
# def disp():
#     l=Label(w,text="Hello World",width=50,bg="green",fg="red")
#     l.pack()
# w=Tk()
# b=Button(w,text="Click!",width=25,bg="yellow",command=disp)
# b.pack()
# w.mainloop()
#
# Q3. Create a frame using tkinter with any label text and two buttons.
# One to exit and other to change the label to some other text.
# Ans-
from tkinter  import *
import sys


# def exit():
#     sys.exit()


# def show():
#     if(t.get()==0):
#        n.set("Hello Python")
#        t.set(1)
#     else:
#         n.set("Hello Java")
#         t.set(0)
#
# def display(r):
#     print(r)
#
#
# root =Tk()
# t = IntVar()
# t.set(0)
#- n=StringVar()
# n.set("Hello World")
# root.title("Windows")
# root.geometry("205x250")
# root.resizable(True,False)
# root.minsize(200,200)
# root.maxsize(300,300)
# l = Label(root, textvariable=n, width=50, bg="dodgerblue", fg="white")
# l.pack()
# b=Button(root,text="Exit",width=25,bg="green",fg="yellow",command=exit)
# b.pack()
#
# b1=Button(root,text="Change",width=25,bg="green",fg="yellow",command=show)
# b1.pack()
#
# b2= Button(root, text="Hello", command=lambda : display(10))
# b2.pack()

# root.mainloop()

# Q4. Write a python program using tkinter interface to
# take an input in the GUI program and print it.
#Ans-
# from tkinter import *
# def show_entry_fields():
#    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# w = Tk()
# Label(w, text="First Name").grid(row=0)
# Label(w, text="Last Name").grid(row=1)
#
# e1 = Entry(w)
# e2 = Entry(w)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# b=Button(w, text='Quit', command=w.quit).grid(row=3, column=0, sticky=W,pady=4,)
#
# c=Button(w, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
#
# mainloop( )
