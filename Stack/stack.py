#stack push pop

stk=[]
size=int(input("Enter the size:"))
top=0

n=0
def push():
    global top,size
    if(top>size):
        print("Stack is full..")
    else:
        p=int(input("Enter the element want to push:"))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print("Stack is empty..")
    else:
        p=int(input("Enter the element want to pop:"))
        stk.pop(p)
        top-=1
def display():
    print(stk)

while(n!=1):
    print("Enter the operation want to perform:")
    opt=int(input("Press 1) Push 2) Pop 3) Display :"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    else:
        display()
    n=int(input("Do you want to continue press 1 for exit"))