student = {
    "name": "Su Su",
    "age" : 20,
    "score": 78,
    "passed": True
}
print(student["name"])
print(student["score"])

student["course"] = "Python for AI"
student["score"] = 97

print(student.get("name"))
print(student.get("grade", "Not assigned"))
print(student)

students = [
 {"name": "Aung Aung", "score": 85},
 {"name": "Su Su", "score": 92},
 {"name": "Mg Mg", "score": 35}
]
for student in students:
 print(student["name"], student["score"])