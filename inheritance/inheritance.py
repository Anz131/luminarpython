#single inheritance

# class Person:                                   #superclass/baseclass/parentclass
#     def persondetails(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Student(Person):                          #derivedclass/subclass/childclass
#     def print(self,dept,clg):
#         self.dept=dept
#         self.clg=clg
#         print(self.dept)
#         print(self.clg)
# per=Person()
# per.persondetails("Anu",22,"Female")
# st=Student()
# st.print("MCA","TASC")
# st.persondetails("Appu",22,"Male")

# class Person:
#     def persondetails(self,id,name,age,gender):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.id)
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Employee(Person):
#     def print(self,dept,job):
#         self.dept=dept
#         self.job=job
#         print(self.dept)
#         print(self.job)
# per=Person()
# per.persondetails(1,"Anu",22,"Female")
# st=Employee()
# st.print("IT","SD")
# st.persondetails(2,"Appu",22,"Male")


# #multiple inheritance
#
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#         print(self.age)
# class Mobile:
#     def print(self):
#         print("I have poco m2")
# class Child(Person,Mobile):                 #2 parent class, person, mobile
#     def info(self,college,place):
#         self.college=college
#         self.place=place
#         print(self.college)
#         print(self.place)
# per=Person()
# per.details("Anu",23)
# mob=Mobile()
# mob.print()
# ch=Child()
# ch.details("Appu",23)
# ch.print()
# ch.info("ABCD","Scotland")

# class Person:
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Employee:
#     def print(self,empid,post):
#         self.empid=empid
#         self.post=post
#         print(self.empid)
#         print(self.post)
# class Staff(Person,Employee):
#     def info(self,salary,experience):
#         self.salary=salary
#         self.experience=experience
#         print(self.salary)
#         print(self.experience)
# per=Person()
# per.details("Anu",23,"Female")
# emp=Employee()
# emp.print(1,"SM")
# st=Staff()
# st.details("Appu",23,"Male")
# st.print(2,"HR")
# st.info(50000,4)


#multilevel inheritance/hierarchial inheritance

# class Person:
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Employee(Person):
#     def print(self,empid,post):
#         self.empid=empid
#         self.post=post
#         print(self.empid)
#         print(self.post)
# class Staff(Employee):
#     def info(self,salary,experience):
#         self.salary=salary
#         self.experience=experience
#         print(self.salary)
#         print(self.experience)
# per=Person()
# per.details("Anu",23,"Female")
# emp=Employee()
# emp.details("Achu",24,"Male")
# emp.print(1,"SM")
# st=Staff()
# st.details("Appu",23,"Male")
# st.print(2,"HR")
# st.info(50000,4)

#person
#child person
#parent person
#student child

# class Person:
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Child(Person):
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
# class Student(Child):
#     def det(self,std,sub):
#         self.std=std
#         self.sub=sub
#         print(self.std)
#         print(self.sub)
# per=Person()
# per.details("Anu",23,"Female")
# ch=Child()
# ch.details("Achu",24,"Male")
# ch.print(1,"SM")
# p=Parent()
# p.details("Appu",23,"Male")
# p.info(50000,4)
# st=Student()
# st.details("Kunju",23,"Female")
# st.print(2,"HR")
# st.det(5,"Python")
