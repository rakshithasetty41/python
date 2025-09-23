#dictionary methods/operations

dict_data={"a":"apple","b":"bananana"}
print(dict_data)

# update() : adds / updates items in dict 
# dict_data.update() 
dict_data.update({"c":"carrot"})
print(dict_data)

#existing key update
dict_data.update({"a":"avacado"})
print(dict_data)

#existing value update
dict_data.update({"c":"cashew"})
print(dict_data)

# pop() : removes the item with key 
#dict_list={"1":10,"2":20,"3":30}
#dict_list("1")TypeError: 'dict' object is not callable
dict_data={"a":"apple","b":"bananana","c":"carrot"}
print(dict_data)
#dict_data.pop() #TypeError: pop expected at least 1 argument, got 0
dict_data.pop("a")
print(dict_data)
#dict_data.pop("d")#KeyError: 'd'
print(dict_data)

#pop() : removes the item with value
dict_data={"a":"apple","b":"bananana","c":"carrot"}
print(dict_data)
#dict_data.pop() #TypeError: pop expected at least 1 argument, got 0
#dict_data.pop("apple")# we cannot pop the values in a dict
print(dict_data)

#popitem():removes the last item
dict_data={"a":"apple","b":"bananana","c":"carrot"}
print(dict_data)
dict_data.popitem()
print(dict_data)
#dict_data.popitem("a")#TypeError: dict.popitem() takes no arguments (1 given)

#clear:empties the dictionary
dict_data={"a":"apple","b":"bananana","c":"carrot"}
print(dict_data)
dict_data.clear()
print(dict_data)
#dict_data.clear("a")#TypeError: dict.clear() takes no arguments (1 given)

#get:used to get the value for a key
dict_data={"a":"apple","b":"bananana","c":"carrot"}
print(dict_data)
#dict_data.get()TypeError: get expected at least 1 argument, got 0
print(dict_data.get("a"))
print(dict_data.get("b"))
print(dict_data.get("apple"))#none becuase we cannot get the values 

# keys() : used to get keys 
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
print(dict_data.keys())
only_key = dict_data.keys()
for key in only_key: 
    print(key)

#copy:make a shallow copy
dict_data={"a":"apple","b":"bananana"}
print(dict_data)
#dict_data.copy("a")TypeError: dict.copy() takes no arguments (1 given)
backup=dict_data.copy()
print(backup)

backup.update({"c":"carrot"})
print(backup)
print(dict_data)

#copy:soft copy
dict_data={"a":"apple","b":"bananana"}
print(dict_data)
backup=dict_data
print(backup)

backup.update({"c":"caluiflower"})
print(dict_data)
print(backup)

# setdefault() : returns value of a key, 
# if not present it sets 
# if key present, will not update 
print("========")
dict_data = {"a":"Apple", "b":"banana"}
print(dict_data)
# dict_data.setdefault() # TypeError: setdefault expected at least 1 argument, got 0
data = dict_data.setdefault("b","blueberry")
print(data)

data=dict_data.setdefault("c","carrot")
print(data)

