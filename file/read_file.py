# read entire file then move cursor to read again
my_single_line_file = open('./files/file.txt')
print(my_single_line_file.read())
# move cursor to the beginning
my_single_line_file.seek(0)
print(my_single_line_file.read())
my_single_line_file.seek(0)
print(my_single_line_file.read())
my_single_line_file.close()

# read line by line
my_multi_line_file = open('./files/file.txt')
print(my_multi_line_file.readline())
print(my_multi_line_file.readline())
print(my_multi_line_file.readline())
# move cursor to the beginning
my_multi_line_file.seek(0)
print(my_multi_line_file.readlines())
my_multi_line_file.close()

# use statement
with open('files/file.txt', mode='r') as my_file:
    print(my_file.read())


# pathlib

# Error handling
try:
    with open('single_line.txt', mode='r') as my_file:
        print(my_file.readline())
except FileNotFoundError as err:
    print('file does not exist')
    # raise err
except IOError as err:
    print('IO error')
    raise err

