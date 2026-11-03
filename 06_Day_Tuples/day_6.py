# Day 6 Tuple

# I
# 1
t = ()

# 2
s = ("A", "B", "C")
b = ("D", "E", "F")
# 3
t = s + b
# 4
print("nr. of siblings: ", len(t))

# 5
p = ("Mom", "Dad")
family_members = t + p

# II
# 1

fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "yogurt")
food_stuff_tp = fruits + vegetables + animal_products

# 2
food_stuff_lt = list(food_stuff_tp)

# 3
print(food_stuff_lt[len(food_stuff_lt) // 2])

# 4
print(food_stuff_lt[0:2])
print(food_stuff_lt[len(food_stuff_lt) - 3 : len(food_stuff_lt) - 1])

# 5
del food_stuff_tp
