num1=int(input("Enter 1st no : "))
num2=int(input("Enter 2nd no : "))
num3=int(input("Enter 3rd no : "))
if(num1>num2 and num1<num3):
    slargest=num1
elif(num2>num1 and num2<num3):
    slargest=num2
else:
    slargest=num3
print("Second Largest no is",slargest)

#also can be done with nested if