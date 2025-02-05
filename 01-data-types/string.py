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
# reverse
print(number[::-1]) # '76543210'

# string is immutability

# string functions
name = 'louis'
print(len(name)) # '5'
print(name[0:len(name)]) # 'louis'

quote = 'to BE or not to be'
print(quote.upper()) # 'TO BE OR NOT TO BE'
print(quote.lower()) # 'to be or not to be'
print(quote.capitalize())  # 'To be or not to be'
print(quote.find('BE')) # 3
print(quote.replace('BE', 'be')) # 'to be or not to be'

sentence = 'himynameislouis'

print(list(sentence)) #['h', 'i', 'm', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'l', 'o', 'u', 'i', 's']

my_list = []
for char in sentence:
    my_list.append(char)
print(my_list) #['h', 'i', 'm', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'l', 'o', 'u', 'i', 's']

print([char for char in 'himynameislouis']) #['h', 'i', 'm', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'l', 'o', 'u', 'i', 's']


# default separator is any whitespace.
sentence2 = 'hi my name is louis'

new_sentence = sentence2.split()
print(new_sentence) # ['hi', 'my', 'name', 'is', 'louis']
joined_sentence = ''.join(new_sentence)
print(joined_sentence) # himynameislouis

# exercise
# birth_year = input('what year were you born?')
# age = 2023 - int(birth_year)
# print(f'Your age is: {age}')

# name = input('Please enter your name: ')
# password = input('Please enter your password: ')
# password_length = len(password)
# hidden_password = '*' * password_length
# print(f'{name}, your password {hidden_password} is {password_length} letters long.')