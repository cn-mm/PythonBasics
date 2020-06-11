x = [i for i in range(5)]  # LIST
x = (i for i in range(5))  # GENERATOR

input_list = [1, 1, 2, 3, 5, 8, 13, 21]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i)) #GENERATOR
[print(i) for i in xyz]


xyz = [i for i in input_list if div_by_five(i)] #LIST
[print(i) for i in xyz]

xyz = []
for i in input_list:
    if div_by_five(i):
        xyz.append(i)

[[print(i,ii) for ii in range(5)] for i in range(5)]

#TIMEIT MODULE
import timeit

#print(timeit.timeit('1+3', number = 500000))


'''
input_list = range(100)
def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

xyz = [i for i in input_list if div_by_five(i)]

'''

print(timeit.timeit(
'''
CODE GOES HERE
''', number = 5000))

