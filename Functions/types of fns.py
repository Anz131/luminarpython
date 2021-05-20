#functions without arguments
#
# def add():
#     num1 = int(input("Enter 1st no : "))
#     num2 = int(input("Enter 2nd no : "))
#     print(num1+num2)
# add()

#function with arguments
#
# def add(a,b):
#     print(a+b)
# add(3,5)

#functipn with arguments and return type
#
# def add(a,b):
#     return (a+b)
# print(add(3,5))

#odd or even

# def oddeven(num):
#     if (num % 2 == 0):
#         print(num, "is even")
#     else:
#         print(num, "is odd")
# oddeven(5)

#positive negative or zero
#
# def pnz(num):
#     if (num > 0):
#         print("Positive")
#     elif(num==0):
#         print("Zero")
#     else:
#         print("Negative")
# pnz(0)

#pattern printing
# ***
# **
# *

# def pattern(n):
#     for i in range(1,n): #no of rows
#         for j in range(i,n):
#             print("*",end=" ")
#         print("\r")
# pattern(5)

 #   *
 #  ***
 # *****
#
# def pattern(n):
#     k=2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-1
#         for j in range(0,i+1):
#             print("*", end=" ")n
#         print("\r")
# pattern(5)





