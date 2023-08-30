# set

# unique value and no index
my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)  # {1, 2, 3, 4, 5, 100}

my_set.discard(100)

new = my_set.copy()
new.clear()
print(new)  # set()
print(my_set)  # {1, 2, 3, 4, 5}

your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))  # {1, 2, 3}
my_set.difference_update(your_set)
print(my_set)  # {1, 2, 3}
my_set.add(4)
my_set.add(5)

print(my_set.intersection(your_set))  # {4, 5}
print(my_set & your_set)  # {4, 5}

print(my_set.isdisjoint(your_set))  # False

print(my_set.union(your_set))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set | your_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

my_set2 = {4, 5}
your_set2 = {4, 5, 6, 7, 8, 9, 10}
print(my_set2.issubset(your_set2))  # True
print(my_set2.issuperset(your_set2))  # False
print(your_set2.issuperset(my_set2))  # True


# Exercise
"""
#using what you learned about sets, create a piece of code that the school principal 
can use to immediately find out who missed class so they can call the parents. 
(Imagine if the list had 1000s of students. The principal can use the lists generated 
by the teachers + the school database to use python and make his/her job easier): 
Find the students that miss class!
"""

school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

attendance = set(attendance_list)


print(f'{school.difference(attendance)} did not attend class')
print(f'{school - attendance} did not attend class')
