#without function

a=10
b=5

#math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=20
b=10
#math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=200
b=100
#math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("="*25)

#with functions  using parameters
def math_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

math_ops(20,10)

a=10
b=5
#calling function
math_ops(a,b)

a=200
b=100
math_ops(a,b)
print("="*25)

#with functions  using parameters
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
a=20
b=10
math_ops()

#a,b are parameters
#20,10 are arguments

#positional arguments

def login(username,password):
    if username=="rakshi" and password=="1234":
        print("login is successful")
    else:
        print("login failed")

login("rakshi","1234")
login("1234","rakshi")
#login()#TypeError: login() missing 2 required positional arguments: 'username' and 'password'
#login("rakshi")TypeError: login() missing 1 required positional argument: 'password'

def employee_info(emp_name,emp_email,emp_loc):
    print(f"This is {emp_name} and emailid is {emp_email} working location is {emp_loc}")

employee_info("rakshi","rakshi@gmail.com","hyderabad")
employee_info("rakshi","hyderabad","rakshi@gmail.com")

print("======================")

#keyword arguments
def employee_info(emp_name,emp_email,emp_loc):
    print(f"This is {emp_name} and emailid is {emp_email} working location is {emp_loc}")

employee_info("rakshi","rakshi@gmail.com","hyderabad")#positional
# passed explicitly by specifying the name
employee_info(emp_email="mahi@gmail.com",emp_loc="pune",emp_name="mahitha")

print("============")

#default arguments
def employee_info(emp_name,emp_email,emp_loc,company_name="google"):
    print(f"This is {emp_name} and emailid is {emp_email} working for {company_name}  and working location is {emp_loc}")
employee_info(emp_email="mahi@gmail.com",emp_loc="pune",emp_name="mahitha")
employee_info(emp_name="kiran",emp_email="kiran@yahoo.com",emp_loc="delhi")
employee_info(emp_name="royal",emp_loc="delhi",emp_email="royal@outlook.com")
employee_info(emp_name="kiran",emp_email="kiran@yahoo.com",emp_loc="kolkata",company_name="amazon")

#arbitary postional arguments(*args)
def add_allnumbers(*numbers):
    total=0
    for num in numbers:
        total+=num
    print(f"the total sum  is {total}")

add_allnumbers(10,20)
add_allnumbers(10,20,30,40)
add_allnumbers(50,40,30,20,10,60,70)

#keyword positional aarguments(**args)
def profile(**info):
    print(info)

profile(name="ravi",age="30",attendence="present")
profile(name="rakshi")
profile(name="rakshi",age=10)

# NOTE : just like dict it's considering only keys 
def credit_trans(**trans):
    print(trans)
    total=0
    for tran in trans:
        print(tran)


credit_trans(jan="20000",feb="10000",mar="50000")

# To get value => we need key 
def credit_trans(**trans):
    print(trans)
    total=0
    for tran in trans:
        print(trans[tran])


credit_trans(jan="20000",feb="10000",mar="50000")


# using both to do some calculations
def cred_trans(**trans):
    print(trans)
    total = 0
    for tran in trans:
        total = total + trans[tran]
        # print(trans[tran])
    print(f"You have done {len(trans)} which amounts to total of {total}")
cred_trans(jan=1000,feb=2000,mar=3000)

#without return
def add(a,b):
    a+b

add(10,20)
print(add(10,20))

#with return
def add(a,b):
    return a+b
add(10,20)
print(add(10,20))


def add(a,b):
    return a+b
    print("See if this will be printed")
    
print(add(10,20))


#here multiple returns are used in the function.but only   first one return will be printed and taken 
def math_ops(a,b):
    return a+b
    return a-b
    return a*b
print(math_ops(200,100))

def math_ops(a,b,opr):
    if opr=="+":
        return a+b
    elif opr=="-":
        return a-b
    elif opr=="*":
        return a*b
    else:
        print("Invalid operators selected")

print(math_ops(20,10,"+"))
print(math_ops(20,10,"-"))
print(math_ops(20,10,"*"))
math_ops(20,10,"/")

#function composition
def add(a,b):
    return a+b
def sub(c,d,e):
    return add(c,d)-e

print(sub(20,10,5))


def student(name):
    return name
def stud(name,age):
    return student(name) ,age

print(stud("rakshi",30))

#local scope
def add():
    la=10
    lb=5
    print(la)# access local variable within function
    print(lb)# access local variable within function
add()
# trying to access local variable outside function
#print(la)

def add(la,lb):
    print(la)
    print(lb)

add(10,20)
# trying to access local variable outside function
#print(la)

#global scope
ga=30
def add(a,b):
    print(a)
    print(b)
    print(ga)
add(10,20)

# name conflict 
ga = 30

def add(la,lb,ga):
    print(la) # access local variable within function
    print(lb) # access local variable within function
    print(ga) # access local variable ga within function
    print(globals()['ga']) # access global variable ga within function
    print(la+lb+ga)

add(1,2,3)

# trying to change global variable 
count = 0
count += 1
print(count)

count = 0
def increment():
    global count
    count += 1 # cannot access local variable 'count'

increment()
print(count)

# Function Types In Python

# get predefined functions 
import builtins
# print(dir(builtins))

# without lambda
def add(a,b):
    return a+b
print(add(3,4))

#lambda
#lamba arguments:expressions
sum=lambda a,b:a+b
print(sum(10,20))

#IILE:Immediately Invoked Lambda Expression
print((lambda a,b:a+b)(10,30))

#without lambda
def even(num):
    if num%2==0:
        return True
    else:
        return False
    
print(even(10))

#with lambda
even=lambda num:num%2==0
print(even(5))
print(even(4))

print((lambda num:num%2==0) (8))
print((lambda num:num%2==0 )(5))

print((lambda num:num%2!=0) (10))
print((lambda num:num%2!=0 )(7))

print((lambda num:"positive" if num >0 else "Negative" if num<0 else "zero")(-10))
print((lambda num:"positive" if num >0 else "Negative" if num<0 else "zero")(10))


employee_info = lambda emp_name,emp_email,emp_location: print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
employee_info("ravi","ravi@gmail.com","hyd")


# Without map()
# Write a script to take a list of numbers and return square of list of number 
# [1,2,3,4,5] => [1,4,9,16,25]

#with function 
def squares_list(numbers):
    square_list=[]
    for num in numbers:
        square_list.append(num*num)
    return square_list
print(squares_list([1,2,3,4,5]))
#with map function
# Write a script to take a list of numbers and return square of list of number 
# [1,2,3,4,5] => [1,4,9,16,25]

print(list(map(lambda num:num*num,[1,2,3,4,5])))

# Without filter()
# Write a script to take a list of numbers and return only even numbers from the list 
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]
def even(numbers):
    even_numbers=[]
    for num in numbers:
        
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
print(even( [1,2,3,4,5,6,7,8,9,10]))

 # Without filter()
# Write a script to take a list of numbers and return only even numbers from the list 
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]

print(list(filter(lambda num: num%2==0,[1,2,3,4,5,6,7,8,9,10])))

# Without reduce()
# Write a script to take a list of numbers and return product of all the items in that list 
# [1,2,3,4,5] => 1*2*3*4*5 = 120

def product(numbers):
    total=1
    for num in numbers:
        total=total*num
    return total
print(product([1,2,3,4,5]))

# With reduce()
# Write a script to take a list of numbers and return product of all the items in that list 
# [1,2,3,4,5] => 1*2*3*4*5 = 120
from functools import reduce
print(reduce(lambda num,total:total*num,[1,2,3,4,5]))

data = [100,None,80,70,None]
print(list(filter(lambda num:num!=None,data)))
print(list(filter(lambda data:data!=None,data)))


servers = ["10.0.0.1","down","10.0.0.3","10.0.0.4","down"]
print(list(filter(lambda servers:servers!="down" ,servers)))
