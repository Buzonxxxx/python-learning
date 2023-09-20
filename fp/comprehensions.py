# list, set
my_list = [char for char in 'hello']
my_list2 = [num for num in range(1, 101)]
my_list3 = [num * 2 for num in range(1, 101)]
my_list4 = [num * 2 for num in range(1, 101) if num % 2 == 0]
print(my_list4)

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
print(dup_list)
