#decorators for more code resuability
#additional features for already existinf fn

#sub

# def dec(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return wrapper
#
#
# @dec
# def sub(n1,n2):
#     return n1-n2
#
# res=sub(5,10)
# print(res)

#div

# def dec(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return wrapper
#
#
# @dec
# def sub(n1,n2):
#     return n1/n2
#
# res=sub(5,10)
# print(res)


def change_pin(user,pin):
    if user=="admin":
        mypin=pin
        return mypin
    else:
        raise Exception("Not able to perform")


def delete(user,username):
    return username+" deleted"

try:
    print(print(change_pin("user1",201348)))
except Exception as e:
    print(e.args)
try:
    print(delete("user1","Anu"))
except Exception as e:
    print(e.args)