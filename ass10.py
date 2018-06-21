# Q.1- Create a class Animal as a base class and define
# method animal_attribute. Create another class Tiger
# which is inheriting Animal and access the base class
#     method.
#Ans-
# class Animal:
#     def show(self):
#         print("Animal")
#
# class Tiger(Animal):
#     def disp(self):
#         print("Tiger")
#
# b=Tiger()
# b.show()
# b.disp()

#Q.2- What will be the output of following code.

# class A:
#     def f(self):
#         return self.g()
#
#     def g(self):
#         return 'A'
#
# class B(A):
#     def g(self):
#         return 'B'
#
# a = A()
# b = B()
# print( a.f(), b.f())
# print (a.g(), b.g())

#Ans-
# First Output=A,B
# Second Output=A,B


# Q.3- Create a class Cop.
#Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details. Create
# another class Mission which extends the class Cop.
# Define method add_mission _details. Select an object
# of Cop and access methods of base class to get
# information for a particular cop and make it available
# for mission.

#Ans-
# class cop:
#     def __init__(self,na,ag,wr,exp,des):
#         self.na=na
#         self.ag=ag
#         self.wr=wr
#         self.exp=exp
#         self.des=des
#
#     def disp(self):
#         print("Person Name=%s"%self.na)
#         print("Age=%d"%self.ag)
#         print("Work=%s"%self.wr)
#         print("Experience=%d"%self.exp)
#         print("Designation=%s"%self.des)
#
#     def update(self):
#         self.na = input("Enter your name:-")
#         self.ag = int(input("Enter your Age:-"))
#         self.wr = input("Enter your work:-")
#         self.exp = int(input("Enter your Experience:-"))
#         self.des = input("Enter your Designation:-")
#
# class mission(cop):
#     def add_mission(self,mis):
#         self.mis=mis
#         print("mission=%s"%self.mis)
#
#
# a = input("Enter your name:-")
# b = int(input("Enter your Age:-"))
# c = input("Enter your work:-")
# d = int(input("Enter your Experience:-"))
# e = input("Enter your Designation:-")
#
# b=mission(a,b,c,d,e)
# b.disp()
# n=input("Enter your mission:-")
# b.add_mission(n)
# m=int(input("if you want to change information,Enter the key Zero"))
# if(m==0):
#     b.update()
#     b.disp()
# else :
#     b.disp()

# Q.4- Create a class Shape.Initialize it with length and
#  breadth Create the method Area. Create class
#  rectangle and square which inherits shape and access
# the method Area.
# Ans-
# class shape:
#     def __init__(self,le,br):
#         self.le=le
#         self.br=br
#
#     def Area(self):
#         self.ar=(self.le)*(self.br)
#         print("Area=%d"%self.ar)
#
# class rect(shape):
#     def Area(self):
#         print("Rectangle")
#         super().Area()
#
# class square(shape):
#     def Area(self):
#         print("Square")
#         super().Area()
#
# l=int(input("Enter your length:-"))
# b=int(input("Enter your breadth:-"))
#
#
# c=square(l,b)
# c.Area()
# b=rect(l,b)
# b.Area()
