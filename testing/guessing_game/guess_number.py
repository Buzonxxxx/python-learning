import random

def run_guess_game(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            print('hey boo, I said 1~10')
            return False
    except TypeError:
        print('please enter a number')
        return False

if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (run_guess_game(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue