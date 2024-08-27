from random import randint
import sys

first_num = int(sys.argv[1])
last_num = int(sys.argv[2])

answer = randint(first_num, last_num)

while True:
    try:
        guess_num = int(input(f'Guess a number {first_num}~{last_num}: '))
        if first_num <= guess_num <= last_num:
            print(f'the answer is: {answer}, you guess: {guess_num}')
            if guess_num == answer:
                print('you are a genius!')
                break
        else:
            print(f'hey bozo, I said {first_num}~{last_num}')
    except ValueError:
        print('please enter a number')
        continue
