
# read and write
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me.')

# append
with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')

# write a new file
with open('new.txt', mode='w') as my_file:
    text = my_file.write('this is a new file')
