# Day 3 - operators

# 1
age = int(21)
# 2
height = float(1.62)
# 3
complex = complex(1 + 2j)
# 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("The area of the triangle is ", 0.5 * base * height)

# 5
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("The perimeter of the triangle is ", a + b + c)

# 6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("The area of the rectangle is ", length * width)
print("The perimeter of the rectangle is ", 2 * (length + width))

# 7
radius = float(input("Enter radius: "))
print("The area of the circle is ", 3.14 * radius**2)
print("The circumference of the circle is ", 2 * 3.14 * radius)

# 8
m1 = 2
y = -2
x = 1
print("The slope is ", m1)
print("The y-intercept is ", y)
print("The x-intercept is ", x)

# 9
m2 = (10 - 2) / (6 - 2)
ed = ((2 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print("The slope is ", m2)
print("The Euclidean distance is ", ed)

# 10
print("Comparison of slopes: ", m1 > m2)

# 11


# 12
print(len("python") > len("dragon"))

# 13
print("on" in "python" and "on" in "dragon")

# 14
print("jargon" in "I hope this course is not full of jargon")

# 15
print("on" not in "python" and "on" not in "dragon")

# 16
print(float(len("python")))
print(str(len("python")))

# 17
a = 8
print("Is", a, "even?", a % 2 == 0)

# 18
print(7 // 3 is int(2.7))

# 19
print(type("10") is type(10))

# 20
print(int(9.8) == 10)

# 21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is ", rate * hours)

# 22
years = int(input("Enter number of years you have lived: "))
print("You have lived for", years * 60 * 60 * 24 * 365, "seconds")

# 23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

for i in range(1, 5):
    print(i**1, i**0, i**1, i**2, i**3)
