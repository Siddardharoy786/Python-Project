students = {
    "Leela":21,
    "Bob":22,
    "Charlie":23,
    "David":24,
    "Eve":25
}

print("Original Dictionary:", students)

students["Frank"] = 26 
print("After Adding:", students)

students["Bobby"]=27
print("After Updating:", students)

print(f"Student {'Leela'}:", students["Leela"])


students = {
    "Leela": {"Age": 21, "Grade": "A"},
    "Bob": {"Age": 22, "Grade": "B"},
    "Charlie": {"Age": 23, "Grade": "A"}
}
print("Nested Dictionary:", students)

print("Details of Leela:", students["Leela"])  
print("Leela's Age:", students["Leela"]["Age"])

print("Keys in the dictionary:", students.keys())

del students["Bob"]
print("After Deleting Eve:", students)

