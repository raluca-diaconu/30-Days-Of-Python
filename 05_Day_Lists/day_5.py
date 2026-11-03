# I.
# 1.
empty = []

# 2.
lista = [1, 2, 3, 4, 5, 6]
# 3
print(len(lista))
# 4
print(lista[0])
print(lista[-1])
print(lista[3])

# 5
mixed_data_types = ["Raluca", 22, 1.6, "single", "adresa 2"]
# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)
# 8
print(len(it_companies))

# 9
print(it_companies[0])
print(it_companies[-1])
print(it_companies[3])

# 10
it_companies[1] = "Googles"
print(it_companies)

# 11
it_companies.append("Tesla")

# 12
it_companies.insert(3, "Al")
# 13
it_companies[1] = it_companies[1].upper()

# 14
it_companies.extend("#,&nbsp;")

# 15
print(it_companies.index("Apple"))
# 16
it_companies.sort()

# 17
it_companies.reverse()

# 18
print(it_companies[0:3])
# 19
print(it_companies[3:6])
# 20
it_companies.slice(3, 4)

# 21
it_companies.pop(0)

# 22
it_companies.pop(int(len(it_companies) // 2))

# 23
it_companies.pop(-1)

# 24
it_companies.clear()

# 25
del it_companies

# 26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

print(front_end + back_end)

# 27
full_stack = front_end + back_end
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")


# II.
# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0])
print(ages[-1])
print(ages[len(ages) // 2])

sum = 0
for i in ages:
    sum += i
print(sum / len(ages))

print("range:", ages[-1], "-", ages[0])
