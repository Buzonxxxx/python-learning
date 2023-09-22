# parameters
# default parameter
def say_hello(name='Darth Vader', emoji=':('):
    print(f'hello {name}, {emoji}')

# arguments
say_hello('Louis', ':)')
say_hello()

# Functions
    # list()
    # print()
    # max()
    # min()
    # input()

# Methods
    # 'hello'.capitalize()

# *agrs **kwargs
# Rule: params, *args, defaul parameters, **kwargs
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func('Louis', 1,2,3,4,5, num1=5, num2=10)) # 30

# exercise
def highest_even(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)
print(highest_even([10,2,3,4,8,11])) # 10

# walrus operator
a = 'helloooooooooo'
# n = len(a)
if (n := len(a)) > 10:
    print(f'too long {n} elements') # too long 14 elements

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
print(a)

# scope
total = 0

def count():
    global total
    total += 1
    return total

count()
count()
print(count()) # 3



