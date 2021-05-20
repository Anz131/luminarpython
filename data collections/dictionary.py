#dictionary = name:value
#keys should not be duplicate, should be unique
#
# dict={'Name':'Anu','Age':'7'}
# print(dict)
# print(type(dict))
#
# print("dict['Name']:",dict['Name'])

#empty dictionary
#
# dit={}
# print(dit)
# print(type(dit))

#update

# dict={'Name':'Anu','Age':'7'}
# dict.update({'loaction':'kannur'})
# dict['Age']=22
# print(dict)

#my dictionary
# dict={}
# dict.update({'Name':'Anu','Age':22,'Location':'Kannur'})
# print(dict)

#remove

# dict={'Name':'Anu','Age':22,'Location':'Kannur'}
# del dict['Age']
# dict.clear()
# del dict
# print(dict)

#program to cjeck a key present in the dictionary
# dict = {'Name': 'Anu', 'Age': 22, 'Location': 'Kannur'}
# key='Age'
# if key in dict:
#     print("present")
# else:
#     print("Not present")

#using fn
# dict = {'Name': 'Anu', 'Age': 22, 'Location': 'Kannur'}
# def dictionary(dict,key):
#     if key in dict:
#         print("present")
#     else:
#         print("Not present")
# dictionary(dict,'Abc')

#count
# dict=input("Enter the stmt:")
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


