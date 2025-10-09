#working with files and directories

#syntax 1
file=open("file.txt","r")
print(file)
print(file.closed)
file.close()
print(file.closed)

#syntax2
with open ("file.txt","r")as file_data:
    print(file_data)
print(file_data.closed)

# Reading Data -> reading whole file content
with open("file.txt","r") as file_data:
    print(file_data.read())

#Reading Data -> reading char wise
with open("file.txt","r") as file_data:
    for char in file_data.read():
        print(char)
#reading data ->reading word wise
with open("file.txt","r")as file_data:
    for words in file_data.read().split():
        print(words)

# Reading Data -> reading line wise 
with open("file.txt","r") as file_data:
    print(file_data.readline())
    print(file_data.readline().strip())

# Reading Data -> reading all lines
with open("file.txt","r") as file_data:
    print(file_data.readlines())
    
with open("file.txt","r") as file_data:
    list_data = file_data.readlines()
    for line in list_data:
        print(line.strip())
        
# Write Mode -> Create File 
with open("write.txt","w") as file_data:
   print(file_data)

#write mode->update
with open("write.txt","w") as file_data:
    file_data.write("hello")

#write mode-> update multiple lines
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line1\n","this is line2"])

#write mode-> update multiple lines
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line3\n","this is line4"])

    
# Write Mode -> Update Multiple Lines Overwrites
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line one \n","this is line two \n"])

#append mode -> updata multiple lines
with open("write.txt","w") as file_data:
    file_data.writelines(["this is line3\n","this is line4"])

# Append Mode -> Update Multiple Lines Appends
with open("new.txt","a") as file_data:
    file_data.writelines(["this is line three \n","this is line four\n"])