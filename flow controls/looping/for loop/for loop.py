#for loop

#initialization
#condition
#incr/decr

#for i in range(lowlimit,upper limit+1, incr/decr):

# for i in range(1,11):  #1 to 10
#     print(i)

#print 10 to 1
# for i in range(10,0,-1):  #1 to 10
#      print(i)

#low limit, upper limit and print
# low=int(input("Enter  lower limit : "))
# up=int(input("Enter  upper limit : "))
# for i in range(low,up+1):
#      print(i)

#lower limit to upper limit even nos

# low=int(input("Enter  lower limit : "))
# up=int(input("Enter  upper limit : "))
# for i in range(low,up+1):
#      if(i%2==0):
#           print(i)

#calculate sum of even and odd nos from lower to upper limit

# low=int(input("Enter  lower limit : "))
# up=int(input("Enter  upper limit : "))
# sumeven=0
# sumodd=0
# for i in range(low,up+1):
#      if(i%2==0):
#           sumeven+=i
#      else:
#           sumodd+=i
# print(sumeven)
# print(sumodd)

#check a given no is prime or not

# num=int(input("Enter a no : "))
# flag=0
# for i in range(2,num):
#      if(num%i==0):
#          flag+=1
# if(flag==0):
#      print("Prime....")
# else:
#      print("Not prime....")

# for i in range(1,4):
#      for j in range(1,4):
#           print(i,end='')
#      print()

# for i in range(1,4):
#      for j in range(1,4):
#           print(j,end='')
#      print()

# for i in range(1,4):
#      for j in range(1,i+1):
#           print(j,end='')
#      print()

#print sum of prime nos upto the limit

# sum=0
# low=int(input("Enter lower limit : "))
# up=int(input("Enter upper limit : "))
# for num in range(low,up+1):
#       if(num>1):
#          for i in range(2,num):
#               if(num%i==0):
#                    break
#          else:
#                print(num)
#               sum+=num
# print(sum)


