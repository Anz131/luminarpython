#to initalize instance variables
#ocnstructor automatically invoke while creating object

# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printval(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# per=Person("anu",22,"female")
# per.printval()

# class Student:
#     college="Luminar"
#     def __init__(self,name,classs,sub,dept):
#         self.name=name
#         self.classs=classs
#         self.sub=sub
#         self.dept=dept
#     def printval(self):
#         print(self.name)
#         print(self.classs)
#         print(self.sub)
#         print(self.dept)
#         print(Student.college)
# st=Student("anu",10,"Python","MCA")
# st.printval()
# st1=Student("appu",10,"Python","MCA")
# st1.printval()

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        print(self.num1)
        print(self.num2)
        print("Sum=",self.num1+self.num2)
    def sub(self):
        print(self.num1)
        print(self.num2)
        print("Sub=",self.num1-self.num2)
    def pdt(self):
        print(self.num1)
        print(self.num2)
        print("Product=",self.num1*self.num2)
    def div(self):
        print(self.num1)
        print(self.num2)
        print("Div=",self.num1/self.num2)

c=Calculator(12,4)
c.sum()
c.sub()
c.pdt()
c.div()
