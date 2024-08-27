from collections import Counter, defaultdict

# Counter
li = [1,2,3,4,5,6,7,7] 
sentence = 'bla bla bla'
print(Counter(li)) # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(Counter(sentence)) # Counter({'b': 3, 'l': 3, 'a': 3, ' ': 2})

# defaultdict
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['a']) # 1
print(dictionary['c']) # does not exist

d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d1['b'] = 2
d1['a'] = 1

print(d1 == d2) # False (different order)



