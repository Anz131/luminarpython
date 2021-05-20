#max among 3 nos


num1=int(input("Enter 1st no : "))
num2=int(input("Enter 2nd no : "))
num3=int(input("Enter 3rd no : "))
# if(num1>num2):
#     if(num1>num3):
#         print(num1,"is greater")
#     else:
#         print((num3,"is greater"))
# else:
#     print(num2,"is greater")

if(num1>num2 and num1>num3):
    print(num1,"is greater")
elif(num2>num1 and num2>num3):
    print(num2,"is greater")
else:
    print(num3,"is greater")

