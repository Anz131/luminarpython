#inheritance using constructor

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# class Student(Person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print(self.rollno)
#         print(self.mark)
# st=Student(2,34,"Anu",22)
# st.printval()
# st.print()

# class Person:
#     def __init__(self,name,age,dept):
#         self.name=name
#         self.age=age
#         self.dept=dept
#     def printval(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Department:",self.dept)
# class Employee(Person):
#     def __init__(self,salary,exp,name,age,dept):
#         super().__init__(name,age,dept)
#         self.salary=salary
#         self.exp=exp
#     def print(self):
#         print("Salary:",self.salary)
#         print("Experience:",self.exp)
# st=Employee(50000,4,"Anu",22,"HR")
# st.printval()
# st.print()

# class Employee():
#     def __init__(self,name,age,dept,salary,exp,):
#         self.name=name
#         self.age=age
#         self.dept=dept
#         self.salary=salary
#         self.exp=exp
#     def print(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Department:",self.dept)
#         print("Salary:",self.salary)
#         print("Experience:",self.exp)
#     def __str__(self):
#         return self.name
# ob=Employee("Anu",22,"HR",50000,4)
# ob.print()
# print(ob)

class Student():
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
    def print(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Dept:",self.dept)
    def __str__(self):
        return self.name+str(self.rollno)
ob=Student("Anu",4,"MCA")
ob.print()
print(ob)

