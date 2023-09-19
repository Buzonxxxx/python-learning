from functools import reduce
# lambda param: action(param)
my_list = [1,2,3]
print(list(map(lambda item: item*2, my_list))) # [2, 4, 6]
print(list(filter(lambda item: item % 2 != 0, my_list))) # [1, 3]
print(reduce(lambda acc, item: acc + item, my_list, 0)) # 6

# square
my_list2 = [5,4,3]
new_list = list(map(lambda item: item * item, my_list2))
print(new_list) # [25, 16, 9]

# List sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a) # [(10, -1), (0, 2), (4, 3), (9, 9)]
