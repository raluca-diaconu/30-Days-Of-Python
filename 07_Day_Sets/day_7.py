#Day 7 Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#I
#1
length=len(it_companies)

#2
it_companies.add('Twitter')

#3
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])

#4
it_companies.remove('IBM')

#5
it_companies.discard('Oracle')

#II
#1
C=A.union(B)

#2
D=A.intersection(B)

#3
isub=A.issubset(B)

#4
disj=A.isdisjoint(B)

#5
E=A.union(B)
F=B.union(A)

#6
sym=A.symmetric_difference(B)

#7
del A, B

#III
#1
ages=set(age)
if(len(ages)>len(age)):
    print("set is smaller than list")

#2


