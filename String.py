# 1. Different ways creating a string

way1 = input()
print(way1)

way2 = "Hello"
print(way2)


way3 = "Hello" + " " + "World"
print(way3)

way4 = 'Using Single Quotetions'
print(way4)

way5 = '''hi 
hello 
bye
'''
print(way5)

# 2. Concatenating two strings using + operator

str1 = "Hello"
str2 = "World"
str3 = str1+" "+str2
print(str3)

# 3. Finding the length of the string

a=input()
print(f"Length of the given string is {len(a)}")

# 4. Extract a string using Substring

a=["I love python","I love java","I love SQL"]
b=input()
for i in a:
    if b in i:
        print(i)
        
# 5. Searching in strings using index()

a=input()
b=int(input("Enter index value:"))
print(a[b])

 # 6. Matching a String Against a Regular Expression With matches()

name = input()

match name:
    case "Mon":
        print("Monday")
    case "Tue":
        print("Tuesday")
    case "Wed":
        print("Wednesday")
    case "Thu":
        print("Thursday")
    case "Fri":
        print("Friday")
    case "Sat":
        print("Saturday")
    case _:
        print("Invalid name was entered")
        
# 7. Comparing strings

a=input()
b=input()
if a == b:
    print(a,"==",b)
else:
    print(a,"!=",b)
    
