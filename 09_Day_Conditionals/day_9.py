# Day 9 - if
# I
# 1
a = int(input("Enter your age: "))
if a < 18:
    print("Wait " + str(18 - a) + " years till you're 18")
else:
    print("You are over 18!!")

# 2
your_age = int(input("Enter your age: "))
my_age = 20

if your_age - my_age > 0:
    print("You are older than me by " + str(your_age - my_age))
    if your_age - my_age > 1:
        print("years")
    else:
        print("year")
elif your_age - my_age == 0:
    print("We are of the same age")
else:
    print("You are younger than me")


# 3
a, b = int(input("a= ")), int(input("b= "))
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")


# II
# 1.
a = int(input("Enter score: "))

if a < 59:
    print("F")
elif a < 69:
    print("D")
elif a < 79:
    print("C")
elif a < 89:
    print("B")
else:
    print("A")

# 2
a = str(input("Enter month: "))
if a == "January" or a == "February" or a == "March":
    print("Winter")
elif a == "April" or a == "May" or a == "June":
    print("Spring")
elif a == "July" or a == "August" or a == "September":
    print("Summer")
elif a == "October" or a == "November" or a == "December":
    print("Autumn")

# 3
fruits = ["banana", "orange", "mango", "lemon"]
a = str(input("Enter fruit name: "))

if a in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(a)
    print(fruits)


# III
# 1
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])

if "skills" in person and "Python" in person["skills"]:
    print("Python is present")

if "JavaScript" in person["skills"] and "React" in person["skills"]:
    print("He is a front end developer")
elif (
    "Node" in person["skills"]
    and "Python" in person["skills"]
    and "MongoDB" in person["skills"]
):
    print("He is a backend developer")
elif (
    "React" in person["skills"]
    and "Node" in person["skills"]
    and "MongoDB" in person["skills"]
):
    print("He is a fullstack developer")
else:
    print("unknown title")

if person["is_married"] and person["country"] == "Finland":
    print(
        person["first_name"]
        + " "
        + person["last_name"]
        + " lives in "
        + person["country"]
        + ". He is married."
    )
