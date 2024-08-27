# for
for item in "Zero to Mastery":
    print(item) # Z e r o   t o   M a s t e r y

# iterable: list, dictionary, tuple, set, string
# iterate dictionary
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item) # name age can_swim

for item in user.keys():
    print(item) # name age can_swim

for item in user.values():
    print(item) # Golem 5006 False

for key, value in user.items():
    print(f'{key}: {value}') # name: Golem age: 5006 can_swim: False


# range()
for _ in range(0, 10, 2):
    print(_) # 0 2 4 6 8

for _ in range(10, 0, -1):
    print(_) # 10 9 8 7 6 5 4 3 2 1

for _ in range(10):
    print(_) # 0 1 2 3 4 5 6 7 8 9

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# enumerate: useful to get index counter
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}') # index of 50 is 50

# while loop: use it when you do not know to many times you want to loop
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i]) # 1 2 3
    i += 1


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

def show_tree():
    fill = '*'
    empty = ' '
    for row in picture:
        for pixel in row:
            if pixel:
                # end: string appended after the last value, default a newline.
                print(fill, end='')
            else:
                print(empty, end='')
        print('') # need a new line after every row

show_tree() 

# find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup_list = []
for char in some_list:
    if some_list.count(char) > 1:
        if char not in dup_list:
            dup_list.append(char)
print(dup_list)




