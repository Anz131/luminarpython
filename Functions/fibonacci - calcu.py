#print the element if present in the string

# a="luminar"
# b=input("Enter the element :  ")
# flag=0
# for i in a:
#     if i in b:
#         flag=1
# if(flag==0):
#     print("Present")
# else:
#     print("Not present")

#print common elements in both strings

# a="anu"
# b="anz"
# for i in a:
#     if i in b:
#         print(i)

#factorial with fn
# def factorial(num):
#     fact=1
#     if(num<0):
#         print("Doesnt exist")
#     elif(num==0):
#         print("1")
#     else:
#         for i in range(1,num+1):
#             fact*=i
#         print(fact)
# factorial(5)

#calculator
#
# def add():
#     a=int(input("Enter 1st no : "))  #float can be used for floating values
#     b = int(input("Enter 2nd no : "))
#     c=a+b
#     print(c)
# def sub():
#     a = int(input("Enter 1st no : "))
#     b = int(input("Enter 2nd no : "))
#     c=a-b
#     print(c)
# def mul():
#     a = int(input("Enter 1st no : "))
#     b = int(input("Enter 2nd no : "))
#     c=a*b
#     print(c)
# def div():
#     a = int(input("Enter 1st no : "))
#     b = int(input("Enter 2nd no : "))
#     c=a+b
#     print(c)
# opt=input("Enter the operation : =,-,*,/ :")
# if(opt=="+"):
#     add()
# elif(opt=="-"):
#     sub()
# elif(opt=="*"):
#     mul()
# elif(opt=="/"):
#     div()
# else:
#     print("Invalid....")

#count no of same elements in the string


# char=input("Enter a character : ")
# string="hellooo"
# count=0
# for i in string:
#     if i in char:
#         count+=1
# print(count)

#move string to another variable
# a="anu"
# b=""
# for i in a:
#     if i not in b:
#         b+=i
# print(b)

#count no of vowels
# str=input("Enter a string : ")
# vowels="aeiou"
# count=0
# for i in str:
#     if i in vowels:
#         count+=1
# print(count)

#remove symbols from string and print
# str=input("Enter a string : ")
# b=""
# char="!@3$%^&*()""'':?~"""
# for i in str:
#     if i not in char:
#         b=b+i
# print(b)

#reverse of a string
# a="abc1234"
# b=a[::-1]
# print(b)

#fibonacci series
# num=int(input("Enter range : "))
# n1=0
# n2=1
# count=0
# while(count<num):
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     count+=1