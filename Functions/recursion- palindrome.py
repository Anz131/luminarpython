#using recursion - a fn calling itself - interview qus
#
# def recur_fibo(n):
#     if n<=1:
#         return n
#     else:
#         return recur_fibo(n-1)+recur_fibo(n-2)
# n_terms=10
# if n_terms<=0:
#     print("please enter a positive integer..")
# else:
#     print("Fibonacci series : ")
#     for i in range(n_terms):
#         print(recur_fibo(i))

#armstrong 407 = 4^3 + 0^3 + 7^3
#
# num=int(input("Enter a no : "))
# sum=0
# temp=num
# while temp>0:
#     dig=temp%10
#     sum+=dig**3
#     temp//=10
# if num==sum:
#     print("Armstrong no...")
# else:
#     print("Not an armstrong no...")

#palindrome

#str=input("Enter a str : ")
# rev=reversed(str)
# if list(str)==list(rev):
#     print("Palindrome..")
# else:
#     print("Not palindrome..")

# str=input("Enter a str : ")
# pal=str[::-1]
# if str==pal:
#     print("Palindromde..")
# else:
#     print("Not palindrome..")


