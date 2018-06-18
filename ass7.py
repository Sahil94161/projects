            #ASSIGNMENT-7
              #FUNCTIONS
      #Let’s create methods for Python.
#Q.1- Create a function to calculate the area of a circle
            #by taking radius from user.
#Ans-
#r=int(input("Enter the radius:-"))
#pi=3.14
#def area():
    #cr=pi*r*r
    #print("Area of circle:- %d "%cr)
#area()

#Q.2- Write a function “perfect()” that determines i
            # f parameter number is a perfect number. Use this
            # function in a program that determines and prints all
            #the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its
            # factors, including 1(but not the number itself), sum to
            # the number. E.g., 6 is a perfect number because
            # 6=1+2+3].
#Ans-

#def perfact(n):
 #   sum=0
  #  for i in range(1,n):
   #     if(n%i==0):
    #        sum=sum+i
    #if sum==n:
     #    print("perfect no:-%d"%sum)


#for x in range(1,1000):
 #   perfact(x)

 #Q.3- Print multiplication table of 12 using recursion.
 #Ans-
#def mul(n,i):
 #   if(i>10):
  #      return 0
   # else:
    #     print("%d*%d=%d"%(n,i,n*i))
     #   return mul(n,i+1)
#mul(12,1)

#Q.4- Write a function to calculate power of a number
            # raised to other ( a^b ) using recursion.
#Ans-
#base= int(input("Enter your base:-"))
#power=int(input("Enter your power:-"))

#def por (x,n):
 #   if(n!=0):
  #      return(x*por(x,n-1))
   # else:
    #    return 1

#n = por(base,power)
#print("%d^%d = %d" %(base, power, n))

#Q.5- Write a function to find factorial of a number but
            # also store the factorials calculated in a dictionary
#Ans-
#n=5
#def rec(x):
 #   if(x==1 or x==0):
  #      return 1
   # else:
    #    f= x*rec(x-1)
     #   return f
#fact=rec(n)
#d={'num':fact}
#print(d)