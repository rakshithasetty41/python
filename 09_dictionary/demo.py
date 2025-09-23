#dictionary

empty_dict={}
print(type(empty_dict))
print(empty_dict)

#using dict class
empty_dict=dict()
print(type(empty_dict))
print(empty_dict)

#acess data
dict={"1":"one","2":"two","3":"three"}
print(dict)

direct_nums={1:10,2:20,3:30}
print(direct_nums)

num_dict={"one":1,2:"two",4:3}
print(num_dict)

text_dict={"bus":"four","train":"many","bike":"two"}
print(text_dict)

#duplicates  for key #not allowed
dict={1:10,2:20,3:30,2:200}
print(dict)

#duplicates for values #allowed
dict={1:10,2:20,3:30,4:20}
print(dict)

#keys cannot mutuable (lists are mutable)
#dict={[10]:100} #TypeError: unhashable type: 'list'
dict={"data":[10,20,30]}
print(dict) 

dict={(10):100}
print(dict)

# dictionary data
students = {
   "101": {
       "name": "Ravi",
       "email": "ravi@gmail.com",
       "course": "Python"
   },
   "102": {
       "name": "Anjali",
       "email": "anjali@gmail.com",
       "course": "Java"
   },
   "103": {
       "name": "John",
       "email": "john@yahoo.com",
       "course": "DevOps"
   }
}

print(type(students))
print(students)

# print(students[0]) # KeyError: 0

# Access data 
# print(students[101]) KeyError: 101
print(students["101"]) 
print(students["101"]["email"])


#want to perform operations
id="103"
if students[id]["email"].endswith("gmail.com"):
    print("google mail id is correct")
else:
    print("only google id accepted")

#looping
dict_nums = {1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[2])


dict_nums={1:10,2:20,3:30}
print(dict_nums)
print(dict_nums[3])

#only we get keys
for data in dict_nums:
    print(data)
print(dir(direct_nums))


