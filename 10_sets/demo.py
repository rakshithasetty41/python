#sets

empty_Set={}
print(type(empty_Set))
print(empty_Set)

empty_Set=set()
print(type(empty_Set))

#nums set
nums_set={10,20,30,40,50}
print(type(nums_set))
print(nums_set) #unordered

#print(nums_set[2]) TypeError: 'set' object is not subscriptable

text_set={"one","two","three"}
print(text_set)

mixed_set={10,20,30,"one","two",40,50}
print(mixed_set)

#loop
for num in nums_set:
    print(num)

print(dir(nums_set)) #sets are mutable

nums_set={10,20,30,40,50}
num_list=list(nums_set)
print(num_list[0])

#frozen set:immutable version of set
fs=frozenset({10,20,30,40,50})
print(type(fs))
print(fs)

print(dir(fs))


#new_set = {list(nums_set),nums_set}
#print(new_set)