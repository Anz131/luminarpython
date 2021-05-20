#overriding - same method name same no of args

# class Parent:
#     def properties(self):
#         print("abcd")
#     def marry(self):
#         print("abc")
# class Child(Parent):
#     def marry(self):
#         print("abc")
# c=Child()
# c.marry()

# class Person:
#     def properties(self,name):
#         self.name=name
#         print(self.name)
#     def ages(self,age):
#         self.age=age
#         print(self.age)
# class Student(Person):
#     def ages(self,age):
#         self.age=age
#         print(self.age)
# c=Student()
# c.ages(22)

# class Person:
#     def properties(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#         print(self.age)
# class Student(Person):
#     def properties(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# f=open("student","r")
# for i in f:
#     data=i.rstrip("\n").split(",")
#     #print(data)
#     name=data[0]
#     age=data[1]
#     c=Student()
#     c.properties(name,age)

# class Person:
#     def properties(self,name,std,dept,mark):
#         self.name=name
#         self.std=std
#         self.dept=dept
#         self.mark=mark
#         print(self.name)
#         print(self.std)
#         print(self.dept)
#         print(self.mark)
# class Student(Person):
#     def properties(self,name,std,dept,mark):
#         self.name=name
#         self.std=std
#         self.dept=dept
#         self.mark=mark
#         print(self.name,self.std,self.dept,self.mark)
# f=open("work","r")
# for i in f:
#     data=i.rstrip("\n").split(",")
#     #print(data)
#     name=data[0]
#     std=data[1]
#     dept=data[2]
#     mark=data[3]
#     if(mark>"190"):
#         c=Student()
#         c.properties(name,std,dept,mark)