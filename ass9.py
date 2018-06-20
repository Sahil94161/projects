#              ASSIGNMENT-10
# Let’s have some fun with classes and objects.

# Q.1- Create a circle class and initialize it with radius.
# Make two methods getArea and getCircumference
# inside this class.
#Ans-

# class Circle:
#     def __init__(self ,rad):
#         self.radius=rad
#     def getArea(self):
#         self.area= 3.14*self.radius*self.radius
#         print("area of circle=%f"%self.area)
#     def getCir(self):
#         self.cir= 2*3.14*self.radius
#         print("circumference of circle=%f"%self.cir)
#
# n=int(input("Enetr the value of radius:-"))
# s=Circle(n)
# s.getArea()
# s.getCir()

#Q.2- Create a Student class and initialize it with name
# and roll number. Make methods to :
#1. Display - It should display all informations of the
#  student.
#Ans-
# class stu:
#     def __init__(self,name,roll):
#         self.na=name
#         self.ro=roll
#
#     def display(self):
#         print("student name:-%s"%self.na)
#         print("student roll number:-%d"%self.ro)
#
# n=input("Enter your name:-")
# r=int(input("Enter your Roll number:-"))
# s= stu(n,r)
# s.display()

# Q.3- Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print
#                 it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will
#               convert it into Celsius.
#Ans-

# class temp :
#     def __init__(self,fah,cel):
#         self.fahr=fah
#         self.cels=cel
#
#     def fahrenheit(self):
#         self.fah=1.8*self.cels+32
#         print("covert to celsius into fahrenheit=%f"%self.fah)
#
#     def celsius(self):
#         self.cel =  (self.fahr - 32)*5/9
#         print("covert  fahrenheit into celsius=%f" % self.cel)
#
# c=int(input("Enter the value of celsius:-"))
# f=int(input("Enter the value of fahrenhiet:-"))
# s= temp(c,f)
# s.fahrenheit()
# s.celsius()

# **Q.4- Create a class MovieDetails and initialize it with
# Movie name, artistname,Year of release and ratings .
# Make methods to
# 1. Display-Display the details.
# 2. Update- Update the movie details.
#Ans-

# class MovieDetails:
#     def __init__(self,na,ar_na,year,ra):
#         self.movie_name=na
#         self.ar=ar_na
#         self.ye=year
#         self.ra=ra
#     def display(self):
#         print("Movie Name:-%s"%self.movie_name)
#         print("Artistname Name:-%s"%self.ar)
#         print("Year of Release:-%d"%self.ye)
#         print("ratings:-%s"%ra)
#
#     def update(self):
#         self.movie=input("Enter the movie name:-")
#         self.ar=input("Enter the Artistname:-")
#         self.ye=int(input("Enetr the year of release:-"))
#         self.ra=input("Enter the value of rating:-")
#
# movie=input("Enter the movie name:-")
# ar=input("Enter the Artistname:-")
# ye=int(input("Enetr the year of release:-"))
# ra=input("Enter the value of rating:-")
#
# s=MovieDetails(movie,ar,ye,ra)
# s.display()
# n=int(input("we you want to change movie details ,Enter the value Zero:-"))
# if(n==0):
#     s.update()
#     s.display()
# else:
#     s.display()

# Q.5- Create a class Expenditure and initialize it with
# expenditure,savings.Make the following methods.
# 1. Display expenditure and savings
# 2. Calculate total salary
# 3. Display salary
#Ans-
class expen:
    def __init__(self,exp,sav):
        self.expe=exp
        self.sa=sav

    def disp(self):
        print("Expenditure=%d"%self.expe)
        print("savings=%d"%self.sa)

    def  cal(self):
        self.sa=self.expe+self.sa

    def dips(self):
        print("Total salary:-%d"%self.sa)

e=int(input("Eneter the value of Expenditure:-"))
s=int(input("Eneter the value of Savings    :-"))
s=expen(e,s)
s.disp()
s.cal()
s.dips()
