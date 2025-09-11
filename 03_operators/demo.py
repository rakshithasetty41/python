#operators
#arithemetic operators
num1=3
num2=2
print(f"sum of{num1}and {num2}is {num1+num2}")
print(f"difference of{num1}and {num2}is {num1-num2}")
print(f"product of{num1}and {num2}is {num1*num2}")
print(f"division of{num1}and {num2}is {num1/num2}")
print(f"modulus of{num1}and {num2}is {num1%num2}")
print(f"floor division of{num1}and {num2}is {num1//num2}")
print(f"power of{num1}and {num2}is {num1**num2}")
#compound assignement operator
num=5
num=num+5 #without using compound assignement operator
print(num)
num3=6
num+=5 #with using compound assignement operator 
num*=5
print(num)

count=1
count+=1 #increment count
print(count)
count=10
count-=1#decrement count
print(count)
#comparison operator
a=10
b=5
c=7
d=9
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(c>=d)
print(d<=c)

#logical operator
p=10
q=5
r=7
s=8
res_and=p>q and s>r
print(res_and)
res_or=p>q or r>s
print(res_or)
res_not=p>q
print(not res_not)
#membership operator
data="python is programming"
is_p_present="p" in data
print(is_p_present)
is_is_present="is " in data
print(is_is_present)
id=106
employees_id=[100,102,103,104,107,108]
is_id_present="id" in employees_id
print(is_id_present)
is_id_not_present="id" in employees_id
print(is_id_not_present)
#identity operator
num1=10
num2=10
print(num1==num2)
print(num1 is num2)
a=[10,20]
b=[10,20]
print(a==b)
print(a is b)
#bitwise operator
a=5
b=3
print(a&b)
print(a|b)
print(a^b)