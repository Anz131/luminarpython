#reduce used when a single output only needed

#import functools

from functools import reduce
lst=[1,2,3,4,5,6]
sum=reduce(lambda num1,num2:num1+num2,lst)
print(sum)

highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(highest)