#grp qus - salary bonus

salary=int(input(("Enter your salary : ")))
service=int(input("Enter year of service"))
if(service>5):
    print("Salary (+bonus)=",salary+(salary)*5/100)
else:
    print(("You are not eligible for the bonus.."))