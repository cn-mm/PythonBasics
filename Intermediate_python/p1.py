names = ['General Kenobi', 'Miles', 'Bill', 'Chet', 'Paul']

for name in names:
    print(''.join(["Hello There, ", name]))

print(', '.join(names)) #print list of names as a string

import os

location_of_files = 'C:\\Users\\Hp\\Desktop\\Wobot\\Intro_to_python'
file_name = 'test.txt'

print(location_of_files + '\\' + file_name )

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

