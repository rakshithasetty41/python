#list related operations

#append it will the at end of the list
num_list=[10,20,30,40,50]
print(num_list)
#num_list.append()#TypeError: list.append() takes exactly one argument (0 given)
num_list.append(70)
print(num_list)
# num_list.append(70,80,90) #TypeError: list.append() takes exactly one argument (3 given)
 
#extend: adds an iterable to the end of the list 
num_list=[10,20,30,40,50]
print(num_list) 
#num_list.extend(60) #TypeError: 'int' object is not iterable
num_list.extend([70,80,90])
print(num_list)

num_list.extend(["employee","hy"])
print(num_list)

num_list.append(["employee","hy"])
print(num_list)

print(num_list[10])
print(num_list[10][1])

## insert() : insert at specific position (index)
num_list=[10,20,30,40,50]
print(num_list)

#num_list.insert(20) #TypeError: insert expected 2 arguments, got 1

num_list.insert(2,70)
print(num_list)

num_list.insert(10,90) # adding at end, if out of range index is given
print(num_list)

num_list.insert(0,5)
print(num_list)

# use assignment operator 
num_list = [10,20,30,40,50] 
print(num_list)
num_list[0] = 5 # Lists are mutable
print(num_list)
 

#pop:remove last element 
num_list=[10,20,30,40,50]
print(num_list)
num_list.pop()
print(num_list)

num_list.pop(3)
print(num_list)
 
#num_list.pop(10) #IndexError: pop index out of range

# remove() : remove element based on value, not index
num_list=[10,20,30,40,50]
print(num_list)
# num_list.remove() # TypeError: list.remove() takes exactly one argument (0 given)
# num_list.remove(0) # ValueError: list.remove(x): x not in list
num_list.remove(30)
print(num_list)

num_list=[10,20,30,40,50,10,70,10,10]
print(num_list)
num_list.remove(10) #remove first occurence
print(num_list)

#remove all occurences
num_list=[10,20,30,40,50,10,70,10,10]
while 10 in num_list:
    num_list.remove(10)
    print(num_list)


# clear() : removes all elements, empties list 
num_list = [10,20,30,40,50,10,70,10] 
print(num_list)
num_list.clear()
print(num_list)


#NOTE : Lists can be modified (Mutable Objects)

# index(): used to get index position of specified value 
num_list = [10,20,30,40,50] 
print(num_list)

#num_list.index() #TypeError: index expected at least 1 argument, got 0
#num_list.index(100) #ValueError: 100 is not in list

print(num_list.index(10))

print(num_list.index(40))

list_nums=[10,20,30,40,20,50,20,60,10,20,10,10]
print(list_nums.index(20))
print(list_nums.index(20,4,8))#4 stop at 8
print(list_nums.index(20,4))#4 stop at end

#count:count the occurences
list_nums=[10,20,30,20,40,20,10,20,10,20,10]
count_10=list_nums.count(10) #TypeError: list.count() takes exactly one argument (0 given)
print(count_10)
print(list_nums.count(40))
print(list_nums.count(80))

#reverse:replaces the list,performance implace operation
num_list=[10,20,30,40]
num_list.reverse()
print(num_list)

num_list=[10,20,30,40]
print(num_list)
reversed_list=num_list[::-1]
print(reversed_list)

#sort:sort the lists,default is ascending order
num_list=[10,50,40,20,30]
print(num_list)

print(num_list.sort())
print(num_list.sort(reverse=True))#descending order
print(num_list)

texted_list=["java","python","c"]
texted_list.sort()
print(texted_list)
mixed_list=[10,20,30,"java",50,"c"]
#mixed_list.sort() #mixed list dont supuort different data types
#print("mixed_list") #TypeError: '<' not supported between instances of 'str' and 'int'

#copy():creates a backup copy (shallow copy),when we modify backup ,orginal copy will not be modified 
num_list=[10,20,30,40,50]
print(num_list)
backup=num_list.copy()
print(backup)
num_list.append(60)
print("orginal",num_list)
print("backup",backup)

#soft copy:when we modify the back up orginal will effect(use=operator)

num_list=[10,20,30,40,50]
print(num_list)
backup=num_list
print(backup)
num_list.append(60)
print("orginal",num_list)
print("backup",backup)