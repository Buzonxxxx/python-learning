# type conversion
print(type(int(str(100)))) # int -> str -> int

# formatted strings
name = "Louis"
age = 39
print(f'hi {name}. You are {age} years old.')
print('hi {}. You are {} years old.'.format(name, age))

# string index
selfish = 'me me me'
         # 01234567
print(selfish[0]) # 'm'
print(selfish[7]) # 'e'

# [start:stop:stepover]
number = '01234567'
print(number[0:2]) # '01'
print(number[0:8:2]) # '0246'
print(number[1:]) # '1234567'
print(number[:5]) # '01234'
print(number[-1]) # '7'
print(number[::-1]) # '76543210'

# string is immutability

# string functions
name = 'louis'
print(len(name)) # '5'
print(name[0:len(name)]) # 'louis'

quote = 'to BE or not ot be'
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.find('BE')) # 3
print(quote.replace('BE', 'be'))

sentence = 'hi my name is louis'
new_sentence = sentence.split()
print(new_sentence) # ['hi', 'my', 'name', 'is', 'louis']
joined_sentence = ''.join(new_sentence)
print(joined_sentence) # himynameislouis

# exercise
# birth_year = input('what year were you born?')
# age = 2023 - int(birth_year)
# print(f'youe age is: {age}')

# name = input('please enter your name: ')
# pw = input('please enter your password: ')
# pw_len = len(pw)
# pw = '*' * pw_len
# print(f'{name}, your password {pw} is {pw_len} letters long.')