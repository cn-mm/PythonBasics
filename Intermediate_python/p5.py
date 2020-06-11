# Writing generators

# Generators yield things

def simple_gen():
    yield '21st'
    yield 'Century'
    yield 'Schizoid'
    yield 'Man'


for i in simple_gen():
    print(i)

CORRECT_COMBO = (2, 4, 0)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield c1, c2, c3


for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo : {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)
