#list
#empty lists
empty_list=[]
print(type(empty_list))
print(empty_list)

#empty lists using list class
empty_list=list()
print(type(empty_list))
print(empty_list)

#list data
num_list=[10,20,30,40,50]
print(num_list)

#list data using list class
num_list=list([10,20,30,40,50])
print(num_list)

text_list=['hyd','django','ai','ml']
print(text_list)
 
text_list=(['hyd','django','ai','ml'])
print(text_list)

mixed_list=[10,20,'hyd','ai',30,40,50]
print(mixed_list)

single_element=[10]
print(single_element)

single_element=list([10])
print(single_element)

#access data
num_list=[10,20,30,40,50]
print(num_list)

#access data individual element
print(num_list[0])
print(num_list[-1])
print(num_list[2])
print(num_list[3])
#print(num_list[10]) #IndexError: list index out of range

## access range of elements use slicing
print(num_list[:])
print(num_list[1:])
print(num_list[0:3])
print(num_list[1:-1])
print(num_list[:-1])
print(num_list[1:10])
print(num_list[::])
print(num_list[1:3:])
print(num_list[0:5:2])
print(num_list[0:10:3])

#list looping
num_list=[10,20,30,40,50] #homogenous
for num in num_list:
    #print(dir(num_list))
    print(num)

#using operators
num_list=[10,20,30,40,50] #homogenous
for num in num_list:
    print(num*5)

#conditional operators
num_list=[10,20,30,40,50]
for num in num_list:
    if (num%2==0):
        print(num)


#duplicates allowed
num_list=[10,20,30,40,50,10,20,10,10] #homogenous
print(num_list)
#print(dir(num_list))



               

