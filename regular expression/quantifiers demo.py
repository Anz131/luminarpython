#quantifiers

#x='a+'     a including group

# import re
# x='a+'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="a*"     count including zero number of a

# import re
# x='a*'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="a?"     count a as each including zero no of a

# import re
# x='a?'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="a{2}"     2 no of a position

# import re
# x='a{2}'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="a{2,3}"     min 2 a and max 3 a

# import re
# x='a{2,3}'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="^a"     check starting with a

# import re
# x='^a'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x="a$"     check ending with a

# import re
# x='a$'
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())