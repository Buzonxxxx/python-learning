# Dictionary

"""
- keys
- values
- items
"""

user = {
    'basket': [1,2,3],
    'greet': 'hello'
}

print(user['basket']) # [1,2,3]
print(user.get('age')) # None
print(user.get('age', 55)) # 55
print(user) # {'basket': [1, 2, 3], 'greet': 'hello'}

# uncommon
user2 = dict(name='Louis')
print(user2) # {'name': 'Louis'}

user3 = user.copy()
print(user3) # {'basket': [1, 2, 3], 'greet': 'hello'}

print('basket' in user3) # True
print('basket' in user3.keys()) # True
print('basket' in user3.values()) # False
user.clear()
print(user3) # {}

user4 = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}
print(user4.pop('age')) # 20
print(user4) # {'basket': [1, 2, 3], 'greet': 'hello'}

user5 = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

user5.update({'age': 55})
user5.update({'agessss': 11})
print(user5) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55, 'agessss': 11}