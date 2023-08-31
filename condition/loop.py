# for
for item in "Zero to Mastery":
    print(item)

# iterable: list, dictionary, tuple, set, string
# iterate dictionary
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for key, value in user.items():
    print(key, value)


# range()
for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for _ in range(10):
    print(_)

print(list(range(10)))

# enumerate: useful to get index counter
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')

# while loop: use it when you do not know to many times you want to loop
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# while True:
#     response = input('say something: ')
#     if response == 'bye':
#         break

# break, continue, pass
for iten in my_list:
    # thinking about it
    pass


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




