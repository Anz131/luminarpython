# current year
# current month
# current date
# dob year
# dob month
# dob date
# calculate age

cyear=int(input("Enter current year : "))  #2021
cmonth=int(input("Enter current month : ")) #03
cday=int(input("Enter current day : ")) #25
print(cday,"/",cmonth,"/",cyear) #25/03/2021
byear=int(input("Enter birth year : ")) #1998
bmonth=int(input("Enter birth month : ")) #07
bday=int(input("Enter birth day : ")) #31
print(bday,"/",bmonth,"/",byear) #31/07/1998
age=cyear-byear
if(cmonth<=bmonth):
    print("Age is",age)
elif(cmonth==bmonth):
    if(cday<bday):
        age-=1
        print("Age is",age)
    else:
        print("Age is",age)
else:
    print("Error....")










