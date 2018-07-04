# Q1. Create a dict with name and mobile number.Define a GUI interface
# using tkinter and pack the label and create a scrollbar to scroll the list
# of keys in the dictionary.
# Ans-
from tkinter  import *

def show():
    d = my.get(ACTIVE)
    print(dict[d])
    l = Label(root, text=d, bg="yellow",width="100")
    l.pack()
    l1 = Label(root, text=dict[d],bg="light green",width="100")
    l1.pack()

dict={}
name=['sahil','nihal','malay','dilpreet','mohit']
number=[9745645,457454,545445,45464,4546545]


for i in range(len(number)):
    dict[name[i]]=number[i]
root =Tk()
w=Scrollbar(root)
w.pack(side=RIGHT,fill=Y)
my=Listbox(root,yscrollcommand=w.set)
for i in dict:
    my.insert(ACTIVE,i)
my.pack(side=LEFT,fill=BOTH)
w.config(command=my.yview)

b=Button(root,text="ClicK!",bg="green",command=show)
b.pack()

root.mainloop()

# Q2. In the same tkinter file as created above, create a function
# to insert items into the dictionary.
# Ans-
# from tkinter import *
#
# def add():
#     dict[str(entry1.get())]=str(entry2.get())
#     print(dict)
#     my.insert(END,str(entry1.get()))
#
# dict={}
# name=['sahil','nihal','malay','dilpreet','mohit']
# number=[9745645,457454,545445,45464,4546545]
# for i in range(len(number)):
#     dict[name[i]]=number[i]
# root =Tk()
# root.geometry("600x200")
# w=Scrollbar(root)
# w.pack(side=RIGHT,fill=Y)
# my=Listbox(root,yscrollcommand=w.set)
# for i in dict:
#     my.insert(ACTIVE,i)
# my.pack(side=LEFT,fill=BOTH)
# w.config(command=my.yview)
#
# entry1=Entry(root)
# entry1.pack()
#
# entry2=Entry(root)
# entry2.pack()
# button=Button(root,text="new entry",command=add,bg="blue")
# button.pack()
# root.mainloop()