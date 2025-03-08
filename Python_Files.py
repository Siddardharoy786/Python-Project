readfile = open("hello.txt",'r')
file = readfile.read()
print(file)

file2 = open('hi.txt','w')
name = "Leelavaraprasad"
file2.write(name)

with open("hello.txt", "r") as file:
    file.seek(1)
    data = file.read(1)
    print("Characters from index 5:", data)
    
import os

file_path = "hello.txt"

if os.access(file_path, os.R_OK):
    print(f"{file_path} has read access")
if os.access(file_path, os.W_OK):
    print(f"{file_path} has write access")
    
    

