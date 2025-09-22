#tuples
#empty lists
empty_tuple=()
print(type(empty_tuple))
print(empty_tuple)

#empty lists using list class
empty_tuple=tuple()
print(type(empty_tuple))
print(empty_tuple)

#list data
num_tuple=(10,20,30,40,50)
print(num_tuple)

#list data using list class
nnum_tuple=tuple((10,20,30,40,50))
print(num_tuple)

text_tuple=tuple(('hyd','django','ai','ml'))
print(text_tuple)
 
text_tuple=('hyd','django','ai','ml')
print(text_tuple)

mixed_tuple=(10,20,'hyd','ai',30,40,50,5.5,True)#hetergoneous
print(mixed_tuple)

single_element=(10)
print(single_element)

single_element=tuple([10])
print(single_element)

#access data
num_tuple=(10,20,30,40,50)
print(num_tuple)

#access data individual element
print(num_tuple[0])
print(num_tuple[-1])
print(num_tuple[2])
print(num_tuple[3])
#print(num_tuple[10]) #IndexError: list index out of range

## access range of elements use slicing
print(num_tuple[:])
print(num_tuple[1:])
print(num_tuple[0:3])
print(num_tuple[1:-1])
print(num_tuple[:-1])
print(num_tuple[1:10])
print(num_tuple[::])
print(num_tuple[1:3:])
print(num_tuple[0:5:2])
print(num_tuple[0:10:3])

#list looping
num_tuple=(10,20,30,40,50) #homogenous
for num in num_tuple:
    #print(dir(num_list))
    print(num)

#using operators
num_tuple=(10,20,30,40,50) #homogenous
for num in num_tuple:
    print(num*5)

#conditional operators
num_tuple=(10,20,30,40,50)
for num in num_tuple:
    if (num%2==0):
        print(num)


#duplicates allowed
num_tuple=(10,20,30,40,50,10,20,10,10) #homogenous
print(num_tuple)
print(dir(num_tuple))


list_orders_id=[101456,547985,987643,56433,986368]
print(type(list_orders_id))
print(list_orders_id)

#unkowingly
list_orders_id.clear()
print(list_orders_id)

list_orders_id=[101456,547985,987643,56433,986368]
read_list_orders_id=tuple(list_orders_id)
print(read_list_orders_id)
num_of_orders=len(read_list_orders_id)
print(num_of_orders)

list_data=list(read_list_orders_id)
print(list_data)




