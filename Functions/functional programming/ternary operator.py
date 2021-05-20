# lst=[7,8,9,4,3,1]
#
# op=[]
#
# for num in lst:
#     if num>5:
#         op.append(num+1)
#     else:
#         op.append(num-1)
# print(op)

# lst=[7,8,9,4,3,1]
# op=[]
#
# for num in lst:
#     op.append((num+1)) if num>5 else op.append((num-1))
# print(op)

# lst=[7,8,9,4,3,1]
#
# op=list(map(lambda num:num+1 if num>5 else num-1,lst))
# print(op)

# num1=10
# num2=20
# high=0
#
# high=num1 if num1>num2 else num2
# print(high)

# lst1=[10,20,21,22,23]
# lst2=[20,21,10,22,23]
# for i in lst1:      #10.20
#     if i in lst2:   #10 in lst2,20 in lst2
#         flag=1      #flag=1, flag=1
#     else:
#         flag=0
# if flag==1:
#     print("Same")
# else:
#     print("Not Same")

lst1 = [10, 20, 21, 22, 23]
lst2 = [20, 21, 10, 22, 23]
lst1.sort()
lst2.sort()
if lst1==lst2:
    print("Same")
else:
    print("Not Same")
