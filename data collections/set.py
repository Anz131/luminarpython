#set
# s={1,2,3,4,5}
# print(s)

#doesnt keep order
# s={1,4,3,2,5}
# print(s)

#type
# a="str"
# print(type(a))

# s={1,2,3,4,5}
# print(s)
# print(type(s))

#empty set

# s=set()
# print(s)
# print(type(s))

#doesnt support duplicates

#add element to set
#supports different types pf data
# s={1,2,3,4,5}
# s.add(6)
# s.add("hello")
# s.add(0.7)
# s.add(True)
# print(s)

# #add using loop
# s=set()
# num1=int(input("Enter 1st range : "))
# num2=int(input("Enter 2nd range : "))
# for i in range(num1,num2+1):
#     ele = input("Enter the element : ")
#     s.add(ele)
# print(s)

#group problem
# def plus_one(x):
#     x+=1
# x=1
# plus_one(x)
# print(x)

# a='pythonbeast'
# if 'p' in a:
#     print('if')
# if 'c' in a:
#     print('if')
# else:
#     print('else')

##remove

# s={1,3,5,7,89,2,3,4,56,6,7,1}
# print(s)
# s.remove(3)
# print(s)

#clear
# s={1,3,5,7,89,2,3,4,56,6,7,1}
# print(s)
# s.clear()
#print(s)

#delete set
# s={1,3,5,7,89,2,3,4,56,6,7,1}
# del s
# print(s)

#nested set
#doesnt support nested set

# s={{1,2,3},{4,5,6}}
# print(s)

#iterate set

# s={1,3,5,7,89,2,3,4,56,6,7,1}
# for i in s:
#     print(i)

#common elements

# s={1,3,5,7,89,2,3,4,56,6,7}
# s1={3,4,5,77,88,9,1}
# for i in s:
#     if i in s1:
#         print(i)

#passed students

# total_stu=("anu","jiya","amal","athul","nandu","aiswarya")
# print(total_stu,"Total students")
# failed={"jiya","amal","nandu"}
# print(failed,"failed students")
# s=set()
# for i in total_stu:
#     if i not in failed:
#         s.add(i)
# print("Passed students ")
# print(s)

#odd and even set
#
# s=(1,4,3,2,5,6,7,8,4,9)
# sodd=set()
# seve=set()
# for i in s:
#     if i%2==0:
#         seve.add(i)
#     else:
#         sodd.add(i)
# print("Odd set",sodd)
# print("Even set",seve)

#prime no set

# s=(1,4,3,2,5,6,7,8,4,9,11)
# sprime=set()
# nonprime=set()
# for i in s:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 nonprime.add(i)
#                 break
#         else:
#             sprime.add(i)
# print("prime set",sprime)
# print("Non prime",nonprime )

#union intersection difference
a={1,5,3,6,7}
b={5,3,4,7,2}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
