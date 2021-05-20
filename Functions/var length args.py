#variable length arguments

#accept any no of args in same method
#using * and return as tuple
#** for key value pair amnd return as dictionary

# def add(*args):
#     print(args)
# add(10)
# add(10,20)
# add(10,20,30)

# def add(*args):
#     res=0
#     for num in args:
#         res+=num
#     return res
# print(add(10,20,30,40))

# arr=[4,3,7,5,9]
# # arr.sort(reverse=True)   #sort the current list
# # print(arr)
# sorted(arr)    #sort into new list
# print(arr)

# def mysortfn():
#     print("Inside sort fn")
#
# class MyList:
#     def mysortmeth(self):
#         print("Inside sort method")
#
# mysortfn()
#
# obj=MyList()
# obj.mysortmeth()

# def print_employee(**kwargs):
#     print(kwargs)
# print_employee(id=100,name="Anu",salary="50000")

employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}

def print_employee(**kwargs):   #kwargs={id:1003,prop="salary"
    id=kwargs["id"]         #1000
    prop=kwargs["prop"]     #salary

    if id in employees:     #1000 in employees
        print(employees[id]["name"])    #employees[1000]
        print(employees[id][prop])      #employees[1000]
    else:
        print("Invalid id")
print_employee(id=1000,prop="salary")

