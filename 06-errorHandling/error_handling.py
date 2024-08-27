while True: 
    try:
        age = int(input('What is your age?\n'))
        10/age
        # raise Exception('hey cut it out')
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

# print(sum(1,0))
# print(sum(1,'0'))