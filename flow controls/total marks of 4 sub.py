#total marks of 4 sub

a=int(input("Enter mark of eng : "))
b=int(input("Enter mark of hin : "))
c=int(input("Enter mark of maths : "))
d=int(input("Enter mark of mal : "))
sum=(a+b+c+d)
print(sum)
if(sum>=180 and sum<=200):   #sum>=180
    print("A+")
elif(sum>=160 and sum<=179):  #160<=sum<=179
    print("A")
elif(sum>=140 and sum<=159):
    print("B+")
elif(sum>=120 and sum<=139):
    print("B")
elif(sum>=100 and sum<=119):
    print("C+")
elif(sum>=80 and sum<=99):
    print("C")
elif(sum>=60 and sum<=79):
    print("A")
else:
    print("Failed....")
