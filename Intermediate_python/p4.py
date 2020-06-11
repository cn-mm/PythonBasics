import timeit

print("Using range: ")
print(timeit.timeit('''
example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    x = (i,example[i])

''', number=500))

print("Using enum")
print(timeit.timeit('''
example = ['left', 'right', 'up', 'down']

for i, j in enumerate(example):
    x = (i,j)

''', number=500))

# Time ranges are similar for both methods


example = ['left', 'right', 'up', 'down']

for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))

# print(new_dict)

# [print(i, j) for i, j in enumerate(new_dict)]

# ZIP
print(" ZIP ")

x = ['a', 'b', 'c', 'd']
y = [2, 3, 4, 8]
z = [6, 2, 9, 4]

for a,b,c in zip(x,y,z):
    print(a,b,c)

print(zip(x,y,z))
print(list(zip(x,y,z)))
print(dict(zip(x,y)))


