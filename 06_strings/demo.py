#strings
#this are single line strings
s1="hello"
#s1=hello #invalid representation
print(s1)

s2='hello'
print(s2)

s3='''hello'''
print(s3)

s4="""hello"""
print(s4)
 
#below are the single line strings

address = """house no 90 
zip is 500081
city is hyderabad"""
print(address)

address = '''house no 90 
zip is 500081
city is hyderabad'''

print(address)

s="how are you"
s1="I'am good "
print(s1)

question="How are you"
answer='I"am good'
print(answer)

question = "How are you ?"
answer = ''' i"m good i'm good '''
print(answer)

text="python"
print(text)

#indexing
# access character -> Index 
print(text[0])
print(text[3])
print(text[-1])
print(text[-2])
print(text[::-1])

# length of string
print(len(text))

    #     0  1  2  3  4  5 (Positive Indexing) (forward)
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

# slicing - slice[start: stop: step]
text = "python"
# print(text[]) # SyntaxError: invalid syntax
print(text[::])
print(text[:])  
print(text[0:5:1])#pytho
print(text[:5:2])
print(text[0:3]) # pyt 
print(text[1:3]) # yt
print(text[1:3:1]) # yt
print(text[0:5:2]) # pto

#     0  1  2  3  4  5 (Positive Indexing) (forward)
#     p  y  t  h  o  n
#    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

print(text[::-1])
print(text[-4:-6:-1])#ty
print(text[-4:-1])#tho
print(text[-4:-1:-1])#empty
print(text[-1:-4:1])#empty
print(text[1:4:-1])#empty
#reverse
text="python"
reversed_text=" "
for char in text:
    reversed_text=char+reversed_text
print(reversed_text)

#string concateion
s="good"
m="morning"
print(s+m)

a=10
b=5
print(a+b)


#string formation
name="rakshi"
age=18
print(f"my name is {name} my age is {age}")
print("my age is:",age)
print("my age is :",+age)
print("my age is :",str(age))
print("my age after 5 years is:",age+5)

#string reptition
laugh="haha"
print(laugh)

hard_laugh="hahahahahahahahahahhaahaha"
print(hard_laugh)

laugh=laugh*5
print(laugh)


greet = "hello"
print(greet)
greet = "Hello"
print(greet)

# String Immutability 
# Immutable : cannot be changed 
greet = "hello"
print(greet)
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet)

print(dir(greet))
