# 1. Write a function to add integer values of an array

a=[]
print("before adding", a)
b=int(input())
a.append(b)
print("After adding", a)

# 2. Write a function to calculate the average value of an array of integers

a=list(map(int, input().split()))
b=sum(a)/len(a)
print(int(b))

# 3. Write a program to find the index of an array element

a=list(map(int, input().split()))
b=int(input())
a.index(b)

# 4. Write a function to test if array contains a specific value

def element_is_available_or_not(arr,b):
    if b in a:
        return "Element is available"
    else:
        return "Element is not available"
arr=list(map(int, input().split()))
b=int(input())
print(element_is_available_or_not(arr,b))

# 5. Write a function to remove a specific element from an array

def remove(arr,b):
    if b in arr:
        arr.remove(b)
arr=list(map(int, input().split()))
b=int(input())
remove(arr,b)
print(*arr)

# 6. Write a function to copy an array to another array

def copy_array(arr):
    copied_array = arr.copy()
    return copied_array

arr=list(map(int, input().split()))
print(arr)
print(copy_array(arr))
    
    
# 7. Write a function to insert an element at a specific position in the array

def insert_element(arr,index,value):
        arr.insert(index,value)
        return arr
arr=list(map(int, input().split()))
index,value=map(int, input().split())
print(*insert_element(arr,index,value))

# 8. Write a function to find the minimum and maximum value of an array

def max_min(arr):
    a=min(arr)
    b=max(arr)
    return a,b
arr=list(map(int, input().split()))
print(*max_min(arr))

# 9. Write a function to reverse an array of integer values

def reverse(arr):
    arr = arr[::-1]
    return arr
arr=list(map(int, input().split()))
print(*reverse(arr))

# 10. Write a function to find the duplicate values of an array

def duplicates(arr):
    for i in arr:
        if arr.count(i) > 1:
            return i
arr=list(map(int, input().split()))
print(duplicates(arr))

# 11. Write a program to find the common values between two arrays

def common_values(arr,arr1):
    a = list(set(arr) & set(arr1))
    return a

arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
print(*common_values(arr,arr1))

# 12. Write a method to remove duplicate elements from an array

def removing_elements(arr):
    arr=list(set(arr))
    return arr

arr=list(map(int, input().split()))
print(*removing_elements(arr))

# 13. Write a method to find the second largest number in an array

def second_largest(arr):
    arr.sort()
    a=arr[-2]
    return a

arr=list(map(int, input().split()))
print(second_largest(arr))

# 15. Write a method to find number of even number and odd numbers in an array

def odd_even(arr):
    even=[]
    odd=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

arr=list(map(int, input().split()))
a,b=odd_even(arr)
print(*a)
print(*b)

# 16. Write a function to get the difference of largest and smallest value

def lar_sml(arr):
    a=max(arr) - min(arr)
    return a

arr=list(map(int, input().split()))
print(lar_sml(arr))

# 17. Write a method to verify if the array contains two specified elements(12,23)

def remove(arr,a,b):
    arr.remove(a),arr.remove(b)
    return arr
arr=list(map(int, input().split()))
a,b=map(int, input().split())
print(*remove(arr,a,b))

# 18. Write a program to remove the duplicate elements and return the new array

def remove_duplicates(arr):
    arr=list(set(arr))
    return arr

arr=list(map(int, input().split()))
print(*remove_duplicates(arr))
