# Ternary Operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message) # message allowed

# Logical Operator
is_magician = False
is_expert = True

if is_magician and is_expert:
    print('your are a master magician')

elif is_magician and not is_expert:
    print('at least yor\'re getting there ')

elif not is_magician:
    print('you need magic powers') # you need magic powers

# ==: check the value
print(True == 1) # True
print('1' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([1,2,3] == [1,2,3]) # True
