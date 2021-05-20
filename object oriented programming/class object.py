#class - design pattern
#objects - real world entity
#reference - name that refers a mem loc ofman obj

#class name first letter caps
#self keyword automatically occur - instance keyword
#many objects can be created in a class using diff ref

# class Person:
#     def walk(self):
#         print("Person is walking..")
#     def jump(self):
#         print("Person is jumping..")
# obj=Person()
# obj.walk()
# obj.jump()
#
# obj2=Person()
# obj2.walk()
# obj2.jump()

# class Vehicle():
#     def car(self):
#         print("Audi")
#     def bike(self):
#         print("RF")
#     def scooty(self):
#         print("Vespa")
#     def bus(self):
#         print("KSRTC")
# obj=Vehicle()
# obj.car()
# obj.bike()
# obj.scooty()
# obj.bus()

# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print(self.name)
#         print(self.age)
# obj=Person()
# obj.details("Anu",22)
# obj.printval()

# class Employee:
#     def details(self,name,id,salary,age,dept,company):
#         self.name=name
#         self.id=id
#         self.salary=salary
#         self.age=age
#         self.dept=dept
#         self.company=company
#     def print(self):
#         print(self.name)
#         print(self.id)
#         print(self.salary)
#         print(self.age)
#         print(self.dept)
#         print(self.company)
# obj=Employee()
# obj.details("Anu",1,50000,22,"GM","TCS")
# obj.print()

#addition pgm using oop

# class Addition:
#     def add(self,a,b):
#         self.a = a
#         self.b = b
#     def print(self):
#         print(self.a)
#         print(self.b)
#         print(self.a+self.b)
# obj=Addition()
# obj.add(2,3)
# obj.print()

#storing same attribute value
#instance variables are related to methods - self
#class variable related to class - college
#instance var called using self - self.name
#class var called using class name - Student.college

# class Student:
#     college="Luminar"
#     def setval(self,name,id):
#         self.name=name
#         self.id=id
#     def printval(self):
#         print("Name : ",self.name)
#         print("Id : ", self.id)
#         print("College : ", Student.college)
# st=Student()
# st.setval("Anu",1)
# st.printval()
#
# st2=Student()
# st.setval("Appu",2)
# st.printval()

# class Employee:
#     company="TCS"
#     def details(self,name,id,salary,age,dept):
#         self.name=name
#         self.id=id
#         self.salary=salary
#         self.age=age
#         self.dept=dept
#     def print(self):
#         print(self.name)
#         print(self.id)
#         print(self.salary)
#         print(self.age)
#         print(self.dept)
#         print(Employee.company)
# obj=Employee()
# obj.details("Anu",1,50000,22,"GM")
# obj.print()
#
# obj=Employee()
# obj.details("Achu",1,50000,22,"GM")
# obj.print()
#
# obj2=Employee()
# obj2.details("Appu",1,50000,22,"SM")
# obj2.print()

class Bank:
    bank="SBI"
    def account(self,accountid,name,age):
        self.accountid=accountid
        self.name=name
        self.age=age
        self.minamt=500
        self.balance=self.minamt
        print("Act ID: ",self.accountid)
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Bank: ", Bank.bank)
        print("minimum amount: ", self.minamt)
        print("Balance",self.balance)
    def deposit(self,depositamt):
        self.depositamt=depositamt
        self.balance+=depositamt
        print("Your ",Bank.bank,"account has been credited with amount",self.depositamt)
        print("Your current balance: ", self.balance)
    def withdrawal(self,withdrawamt):
        self.withdrawamt=withdrawamt
        if self.depositamt>self.balance:
            print("Insufficient balance..")
        else:
            print("Your account has been debited with",self.withdrawamt)
            self.balance-=self.withdrawamt
            print("Available balance:",self.balance)
b=Bank()
b.account(1,"Anu",22)
b.deposit(9500)
b.withdrawal(4000)
