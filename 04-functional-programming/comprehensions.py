# list, set
my_list = [char for char in 'hello']
print(my_list) # ['h', 'e', 'l', 'l', 'o']

my_list2 = [num for num in range(1, 21)] 
print(my_list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

my_list3 = [num * 2 for num in range(1, 21)]
print(my_list3) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

my_list4 = [num * 2 for num in range(1, 21) if num % 2 == 0] 
print(my_list4) # [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

# dictionary
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = { k:v**2 for k,v in simple_dict.items() if v % 2 == 0 }
my_dict1 = { num:num*2 for num in [1,2,3]}
print(my_dict) # {'b': 4}
print(my_dict1) # {1: 2, 2: 4, 3: 6}

# find duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup_list = list(set([char for char in some_list if some_list.count(char) > 1]))
print(dup_list) # ['b', 'n']
