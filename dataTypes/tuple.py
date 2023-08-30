# Tuple is an immutable List
my_tuple = (1,2,3,4,5)
print(my_tuple[1]) # 2
print(5 in my_tuple) # True

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])

print(my_tuple[1:4]) # (2, 3, 4)
print(my_tuple.count(1)) # 1
print(my_tuple.index(4)) # 3
print(len(my_tuple)) # 5
