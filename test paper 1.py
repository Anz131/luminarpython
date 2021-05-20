#1 sort and eliminate duplicate elements in the list

# a=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# duplicte={1,0,7,5,9,2,3,5,7,2,0,1,10}
# unique=[]
# for i in a:
#     if i in duplicte:
#         unique.append(i)
#         duplicte.add(i)
# print(duplicte)

# a=[1,2,4,3,6,2,7,3,8,4]
# b = list(set(a))
# print(b)

#2 dictionary

# dict= "When making changes to the source code that programs are made up of programmers need to make other programmers aware of the task that the routine is to perform They do this by inserting comments in the source code so that others can understand the program more easily and by documenting their code To save work programmers often use libraries of basic code that can be modified or customized for a specific application This approach yields more reliable and consistent programs and increases programmers productivity by eliminating some routine steps"
# count={}
# words=dict.split(" ")
# for word in words:
#     if word not in count:
#         count.update({word:1})
#     else:
#         val=int(count[word])
#         val+=1
#         count.update({word:val})
# print(count)

# count={}
# f=open("fil","r")
# for n in f:
#     wr=n.split(" ")
#     print(wr)
#     for word in wr:
#         if word not in count:
#             count.update({word:1})
#         else:
#             val=int(count[word])
#             val+=1
#             count.update(({word:val}))
# print(count)

#3 second largest element from the list
# lst= [3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# max = max(lst[0], lst[1])
# secondmax = min(lst[0], lst[1])
# n = len(lst)
# for i in range(2, n):
#     if lst[i] > max:
#         secondmax = max
#         max = lst[i]
#     elif lst[i] > secondmax and max != lst[i]:
#         secondmax = lst[i]
# print("Second highest number is : ",str(secondmax))

# lst= [3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print(lst[-2])

#4 common elements from 2 list

# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# for i in a:
#     if i in b:
#         print(i)

#5 max salary list details
#
lst = [(1, "anu", 28, 20000), (2, "vinu", 23, 15000), (3, "ram", 25, 10000)]
# lst.sort()
# print(lst[-1])
for i in lst:
    if (i[3]>=15000):
        print(i)
