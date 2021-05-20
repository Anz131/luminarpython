employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vijay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]


# print employee names only map()

# names=list(map(lambda name:name["name"],employees))
# print(names)


#print all employee name into uppercase  map()

# names=list(map(lambda name:name["name"].upper(),employees))
# print(names)


#print employee details whose name starting with 'a'   ==a  filter()

# names=list(filter(lambda name:name["name"][0]=="a",employees))
# print(names)


#print employee details whode salary > 23000  filter()

# names=list(filter(lambda name:name["salary"]>23000,employees))
# print(names)


#print employee details whose designation==developer

# names=list(filter(lambda name:name["designation"]=="developer"and name["salary"]>23000,employees))
# print(names)

# from functools import reduce
# highest=reduce(lambda sal1,sal2:sal1 if sal1>sal1 else sal2,
#                     list(map(lambda emp:emp["salary"],employees)))
# print(highest)

#using list comprehension

# enames=[emp["name"] for emp in employees]
# print("Names-------",enames)

# enames=[emp["name"].upper() for emp in employees]
# print("Names-------",enames)

# enames=[emp["name"] for emp in employees if emp["name"][0]=="a"]
# print("Names-------",enames)

# salary=[emp for emp in employees if emp["salary"]>23000]
# print(salary)