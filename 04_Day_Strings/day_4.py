# Day 4 - strings

# 1.
s1 = "Thirty"
s2 = "Days"
s3 = "Of"
s4 = "Python"
s5 = s1 + " " + s2 + " " + s3 + " " + s4
print(s5)
# 2
s1 = ["Coding", "For", "All"]
print(" ".join(s1))
# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))
# 6
print(company.upper())
# 7
print(company.lower())
# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9
print(company[0:5])
print(company.split())
# 10
print(company.find("Coding"))
# 11
print(company.replace("Coding", "Python"))
# 12
s = "Python For Everyone"
s = s.replace("Everyone", "All")

# 13
print(" ".split(company))

# 14
s = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s.split(","))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
print(company[0] + company[7] + company[-3])


# 20
print(company.index("C"))
# 21
print(company.index("F"))
# 22
print(company.rindex("l"))
# 23
print(
    "You cannot end a sentence with because because because is a conjunction".index(
        "because"
    )
)

# 24
print(
    "You cannot end a sentence with because because because is a conjunction".rindex(
        "because"
    )
)

# 25
print("You cannot end a sentence with because because because is a conjunction".split)

# 28
print(company.startswith("Coding"))
# 29
print(company.endswith("coding"))
# 30
print(company.strip())

# 31
print("30DaysOfPython".isidentifier())

# 32
s = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(s))

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 36
a = 8
b = 6
print("{ } + { } = {}".format(a, b, a + b))
print("{ } - { } = { }".format(a, b, a - b))
print("{ } * { } = { }".format(a, b, a * b))
print("{ } / { } = {:.2f}".format(a, b, a / b))
print("{ } % { } = { }".format(a, b, a % b))
print("{ } // { } = { }".format(a, b, a // b))
print("{ } ** { } = { }".format(a, b, a**b))
