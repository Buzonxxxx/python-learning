# list is muatable

# list slicing
cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(cart[0:2]) # ['notebooks', 'sunglasses']

# from index 0 and going up to the end of the list, with a step size of 2.
print(cart[0::2]) # ['notebooks', 'toys']

# copy list
new_cart = cart[:]
new_cart[0] = 'gum' 
print(new_cart) # ['gum', 'sunglasses', 'toys', 'grapes']
print(cart) # ['notebooks', 'sunglasses', 'toys', 'grapes']

# adding
basket = [1,2,3,4,5]
basket.append(6)
print(basket) # [1, 2, 3, 4, 5, 6]

basket.insert(4, 100)
print(basket) # [1, 2, 3, 4, 100, 5, 6]

basket.extend([7, 8, 9, 10])
print(basket) # [1, 2, 3, 4, 100, 5, 6, 7, 8, 9, 10]

# sum
print(sum(basket)) # 136

# removing
# pop() 有return value
basket1 = [1,2,3,4,5]
print(basket1.pop()) # 5
print(basket1) # [1,2,3,4]

print(basket1.pop(0)) # 1
print(basket1) # [2,3,4]

basket1.remove(2)
print(basket1) # [3,4]

basket1.clear()
print(basket1) # []

# index
# index() 有return value
basket2 = ['a','b','c','d','e']
print(basket2.index('a')) # 0
print(basket2.index('d', 0, 4)) # 3

print('a' in basket2) # True

# count
print(basket2.count('d')) # 1

# sort() 會改變原本list
basket3 = ['a','b','c','d','e','d']
basket3.sort()
print(basket3) # ['a', 'b', 'c', 'd', 'd', 'e']

# sorted() 不會改變原本list
basket4 = ['a','b','c','d','e','d']
print(sorted(basket4)) # ['a', 'b', 'c', 'd', 'd', 'e']
print(f'basket4: {basket4}') # ['a', 'b', 'c', 'd', 'e', 'd']

basket5 = ['a','b','c'] 
basket5.reverse()
print(basket5) # ['c', 'b', 'a']
print(basket5[::-1]) # ['a', 'b', 'c'] 轉回來
print(basket5) # ['c', 'b', 'a']

# create list with ele from 1 to 100
print(list(range(1,101)))

# create list with 100 'nemo'
large = ['nemo' for i in range(100)]
large2 = ['nemo'] * 100
print(large)
print(large2)
print(large == large2) # True

# list unpacking
a, b, c, *other, d = [1,2,3,4,5,6,7]
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4,5,6]
print(d) # 7