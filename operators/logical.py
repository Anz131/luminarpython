#logical operators

num1=2
num2=5
print(num1&num2)
#result=0

print(num1|num2)
#                            AND  OR   XOR
#result=7                  0 0    0    0    0
#                          0 1    0    1    1
#2 0010                    1 0    0    1    1
#5 0101                    1 1    1    1    0
#-----------AND
#  0000  (0)
#-----------OR
#  0111  (7)

#XOR
print(num1^num2)
#same value then 0 else 1

# 0010  (2)
# 0101  (5)
#--------
# 0111  (7)
