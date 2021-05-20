# import re
# n="helloo"
# x='\w*'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

# import re
# n="56kg"
# x='\d{2}[a-z]{2}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

# import re
# n="+918075694088"
# x='[+][9][1]\d{10}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

# import re
# f2=open("validreg","w")
# rule="[L][U][M]\d{2}[P][Y]\d{3}$"
# f=open("lum","r")
# for num in f:
#     number=num.rstrip("\n")
#     matcher=re.fullmatch(rule,number)
#     if matcher!=None:
#         f2.write(number)
#         f2.write("\n")