#methods 
#add: add element to a set
s1={10,20,30,40,50}
print(s1)
#s1.add() #TypeError: set.add() takes exactly one argument (0 given)
s1.add(60)
print(s1)

# update() : add multiple elements(iterables) to set 
s1={10,20,30,40,50}
print(s1)
s1.update([60,70,80])
print(s1)


#remove:remove elements
s2={10,20,30,40}
print(s2)
#s2.remove() TypeError: set.remove() takes exactly one argument (0 given)
s2.remove(10)
print(s2)

# discard() : remove element if found, no error if not found
s1={10,20,30,40,50}
print(s1)
s1.discard(50)
print(s1)
s1.discard(60)
print(s1)

#pop:removes random element 
s1={10,20,30,40,50}
print(s1)
#s1.pop(20) TypeError: set.pop() takes no arguments (1 given)
s1.pop()
print(s1)
s1.pop()
print(s1)

#clear
s1={10,20,30,40,50}
print(s1)
s1.clear()
print(s1)

s1={10,20,30,40,50}
print(s1)
list1=list(s1)
list1.sort()
print(list1[0])

#copy:
s1={10,20,30,40,50}
print(s1)
backup=s1.copy()
print(backup)

backup.pop()
print(backup)
print(s1)

backup.update([60,70,80])
print(backup)
print(s1)

#softcopy:
s1={10,20,30,40,50}
print(s1)
backup=s1
print(backup is s1)
print(backup)

backup.pop()
print(backup)
print(s1)

#sets are mutable above methods confirm that
s1={10,20,30,40,50,60,10,20,30}
print(s1)

print("========")
#special functions for set
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1)
print(s2)

#union:combine both sets
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

#intersection:extract commmon elements
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1 & s2)

# intersection_update() : extract common elements, also update the calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)


#difference:remove the  common elements
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1-s2)
print(s1.difference(s2))
print(s1)
print(s2)

#difference_update:remove the  common elements, also update calling set
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

#symmetric_difference : removes common elements and takes the combined elements left in both
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

#symmetric_differenc update:removes common elements and takes the combined elements left in both,also update calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

#subset:check if the given set is subset of another set
s1={10,20,30,40,50}
s2={30,40}
s3={10,20}
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s3.issubset(s1))

#superset:check if given set is a superset of another set
print(s1.issuperset(s2))
print(s1.issuperset(s3))

#disjoint:check if two sets has no common elements
s4={90,100}
print(s1.isdisjoint(s2))
print(s3.isdisjoint(s1))
print(s4.isdisjoint(s1))
print(s1.isdisjoint(s4))