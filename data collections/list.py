#list

# define using sq bracket[]
# seperate using comma ,
# no order, only as given order

# type
#suppors diff types

# lst=[2,5,3,5,78,6]
# print(lst)
# print(type(lst))

#append to add
# lst=[]
# lst.append("name")
# lst.append(0.7)
# print(lst)

#remove
# lst=[2,5,3,5,78,6]
# lst.remove(78)
# print(lst)

#clear

# lst=[2,5,3,5,78,6]
# lst.clear()
# print(lst)

#delete
# lst=[2,5,3,5,78,6]
# del lst
# print(lst)

#support duplicate
# lst=[2,5,3,5,78,6]
# print(lst)

#support nested list

# lst=[[2,5,3,[8,9,10]],[5,78,6]]
# for i in lst:
#     print(i)
#iterate
# lst=[[2,5,3,[8,9,10]],[5,78,6]]
# for i in lst:
#     print(i)

#multiply elements
# l=[1,2,3,4]
# mul=1
# for i in l:
#     mul=mul*i
# print(mul)

#odd and even
# l=[1,4,3,2,5,6,7,8,4,9]
# lodd=[]
# leve=[]
# for i in l:
#     if i%2==0:
#         leve.append(i)
#     else:
#         lodd.append(i)
# print("Odd list",lodd)
# print("Even list",leve)

#prime
# s=(1,4,3,2,5,6,7,8,4,9,11)
# sprime=[]
# nonprime=[]
# for i in s:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 nonprime.append(i)
#                 break
#         else:
#             sprime.append(i)
# print("prime list",sprime)
# print("Non prime",nonprime )

#extend
# mylst=[1,2,3,4,5]
# anthrl=["jhjjd","hdjj","jjdj"]
# mylst.extend(anthrl)
# print(mylst)

# s=[1,4,3,2,5,6,7,8,4,9,11]
# s.sort()
# print(s)