# Day 10 loops
# I

# 1

for i in range(11):
    print(i)
i = 0
while i <= 10:
    print(i)
    i += 1

# 2
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1


# 3
for i in range(0, 7, 1):
    for j in range(0, i, 1):
        print("#", end="")
    print("\n")

# 4
for i in range(1, 8, 1):
    for j in range(1, 8, 1):
        print("# ", end="")
    print("\n")

# 5
for i in range(0, 11, 1):
    print(i, "x", i, "=", i * i)
    print("\n")

# 6
list = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for i in list:
    print(i)

# 7
for i in range(0, 101, 2):
    print(i)

# 8
for i in range(1, 100, 2):
    print(i)

# II
# 1
s = 0
for i in range(0, 101, 1):
    s += i
print("The sum of all numbers from 0 to 100 is:", s)

# 2
sp = 0
si = 0
for i in range(0, 101, 1):
    if i % 2 == 0:
        sp += i
    else:
        si += i

print("The sum of all even numbers from 0 to 100 is:", sp)
print("The sum of all odd numbers from 0 to 100 is:", si)


# III
# 1
fruit = ["banana", "orange", "mango", "lemon"]
r = []
for i in range(len(fruit), 0, -1):
    r.append(fruit[i - 1])

print(r)
