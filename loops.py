# Write a program to print “Bright IT Career” ten times using for loop

for i in range(10):
    print("Bright TI Career")
   
# Write a python program to print 1 to 20 numbers using the while loop. 
i=1
while i<=20:
    print(i,end=" ")
    i+=1
   
# Program to equal operator and not equal operators
 
a,b = map(int, input().split())
if a==b:
    print("a == b")
else:
    print("a != b")
    
# Write a program to print the odd and even numbers 

a=int(input())

if a%2==0:
    print(a,"is an even number")
else:
    print(a,"is a odd number")
    
# write a program to print largest number among three numbers.

a,b,c = map(int, input("Enter your 3 numbers with spaces").split())
if a>b and a>c:
    print(a,"is largest number")
elif b>a and b>c:
    print(b,"is largest number")
else:
    print(c, "is largest number")
    
#  Write a program to print even number between 10 and 20 using while

i=10
while i<=20:
    if i%2==0:
        print(i,end=" ")
    i+=1
    
#  Write a program to print 1 to 10 using the do-while loop statement.

i=1
while True:
    print(i,end=" ")
    i+=1
    if i>=21:
        break
    
# Write a program to find Armstrong number or not

a=input()
temp=int(a)
sum=0
for i in a:
    i=int(i)
    sum+=i**len(a)
if sum==temp:
    print(a,"Armstrong Number")
else:
    print(a,"Not an armstrong number")
    
# Write a program to find the prime or not.

def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False 
    return True  
num = int(input("Enter a number: "))
if is_prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
# Write a program to palindrome or not.

n=int(input())
temp=n
s=0
while n!=0:
    r=n%10
    s = s*10 + r
    n=n//10
if temp==s:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Program to check whether a number is EVEN or ODD using switch
a=int(input())
a=a%2
match (a) :
    case 1 :
        print("ODD")
    case _:
        print("EVEN")
    

  
