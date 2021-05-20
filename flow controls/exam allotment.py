#exam allotment - group qus

num1=int(input("Enter the no of classes held : "))
num2=int(input("Enter the no of classes attended : "))
avg=(num2/num1)*100
print(avg)
if(avg>=75):
    print(("allowed...."))
else:
    print("Not allowed....")
