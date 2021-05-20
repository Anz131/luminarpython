#1. bus class - child class

# class Vehicle:
#     def details(self,name,color):
#         self.name=name
#         self.color=color
#         print(self.name)
#         print(self.color)
# class Bus(Vehicle):
#     def print(self,name,num,regplace):
#         self.name=name
#         self.num=num
#         self.regplace=regplace
#         print(self.name)
#         print(self.num)
#         print(self.regplace)
# v=Vehicle()
# v.details("Car","Pink")
# b=Bus()
# b.details("BUS","Blue")
# b.print("LIMRAS","KL 19 R 1073","Taliparamba")

#2. three types of inheritance

# class Person:
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Sub:
#     def sprint(self,mob,address):
#         self.mob=mob
#         self.address=address
#         print(self.mob)
#         print(self.address)
# class Child(Person,Sub):
#     def print(self,empid,post):
#         self.empid=empid
#         self.post=post
#         print(self.empid)
#         print(self.post)
# class Parent(Person):
#     def info(self,salary,experience):
#         self.salary=salary
#         self.experience=experience
#         print(self.salary)
#         print(self.experience)
# class Student(Parent):
#     def det(self,std,sub):
#         self.std=std
#         self.sub=sub
#         print(self.std)
#         print(self.sub)
# per=Person()
# per.details("Anu",23,"Female")
# s=Sub()
# s.sprint("1234567890","Kannur")
# ch=Child()
# ch.details("Achu",24,"Male")
# ch.sprint("9087654321","Payyanur")
# ch.print(1,"SM")
# p=Parent()
# p.details("Appu",23,"Male")
# p.info(50000,4)
# st=Student()
# st.details("Kunju",23,"Female")
# st.info(75000,6)
# st.det(5,"Python")

#3. book class with instance library_name,book_name,author,pages

# class Book:
#     language="English"
#     def details(self,Library_name,book_name,author,pages):
#         self.Library_name = Library_name
#         self.book_name = book_name
#         self.author = author
#         self.pages = pages
#     def printval(self):
#         print("Libray_name",self.Library_name)
#         print("book_name",self.book_name)
#         print("author",Book.language)
# b=Book()
# b.details("ABCLibrary","Knock Out","Luther Cruiz",400)
# b.printval()

#4. animal class -child class dog

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("Name:",self.name)
#         print("Age:",self.age)
# class Dog():
#     def dogmod(self,mod,color):
#         self.mod=mod
#         self.color=color
#         print("Mode:",self.mod)
#         print("Color:",self.color)
# class Pom(Dog):
#     def features(self,name,age,color):
#         self.name=name
#         self.age=age
#         self.color=color
#         print(self.name)
#         print(self.age)
#         print(self.color)
# d=Dog()
# d.dogmod("Pug","Brown")
# p=Pom()
# p.dogmod("Pom","Black")
# p.features("Julie",1,"white")

#5. method overriding - book class

# class Book:
#     def properties(self,name):
#         self.name=name
#         print(self.name)
#     def ages(self,age):
#         self.age=age
#         print(self.age)
# class Author(Book):
#     def ages(self,age):
#         self.age=age
#         print(self.age)
# auth=Author()
# auth.ages(22)

#6. create objects wuth  anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195 and print details with max mark

# class Student:
#     def properties(self,name,std,dept,mark):
#         self.name=name
#         self.std=std
#         self.dept=dept
#         self.mark=mark
#         print(self.name)
#         print(self.std)
#         print(self.dept)
#         print(self.mark)
#     def __init__(self):
#         return  self.name
# f=open("objects","r")
# lst=[]
# for line in f:
#     data=line.rstrip("\n").split(",")
#     lst.append(data)
# print(lst)
# for i in lst:
#     a=(int(i[3]))
#     print(a)
# for i in range(0,len(lst)):
#     for j in range(0,len(lst) - i - 1):
#         if lst[j][-1]>lst[j+1][-1]:
#             temp=lst[j]
#             lst[j]=lst[j+1]
#             lst[j+1]=temp
# print("Details of student with highest mark is:",lst[-1])

#7. valid ph nos from file +915678905432 +914567890321 765432167 123450987765 +919976532456

# import re
# f=open("phonenum","r")
# l=[]
# for i in f:
#     x="^[+][9][1][0-9]{10}"
#     n=re.findall(x,i)
#     if n!=[]:
#         l.append(n)
#         f=open("num","w")
#         f.write(str(l))

# import re
# r=open("phonenum","r")
# f=open("num.txt","w")
# x="[+][9][1]\d{10}$"
# for num in r:
#     number=num.rstrip("\n")
#     matcher=re.fullmatch(x,number)
#     if matcher != None:
#         f.write(number)
#         f.write("\n")

#8. finally block

# try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
# except:
#     print("Exception occured..")
# finally:
#   print("In finally..")

#9. sequence of 1 uppercase letter followed by lowercase

# import re
# n="Anu"
# x="[A-Z][a-z]*"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#10. string with a followed by ending with b

# import re
# n="anjb"
# x='(^a[a-zA-Z0-9\W]*b$)'
# match=re.fullmatch( x , n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
