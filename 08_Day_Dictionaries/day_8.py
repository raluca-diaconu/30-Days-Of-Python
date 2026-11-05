# Day 8 Dictionaries

# 1
dog = {}

# 2
dog = {"name": "Ana", "breed": "Da", "legs": 4, "age": 3}

# 3
student = {
    "first_name": "Ana",
    "last_name": "Lol",
    "gender": "female",
    "age": 10,
    "maritalstatus": "false",
    "skills": [1, 2, 3],
    "country": "Anaaaa",
    "city": "Buc",
    "address": "Str pad",
}

# 4
print(len(student))

# 5
m = student["skills"]
print(type(m))

# 6
student["skills"].append(7)
student["skills"].append(8)
# 7
l = list(student.keys())

# 8
li = list(student.values())

# 9
list = student.items()

# 10
student.popitem()

# 11
del student
