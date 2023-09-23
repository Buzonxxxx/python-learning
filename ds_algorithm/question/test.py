# //Google Question
# array = 
# //It should return 2


# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return None


def firstRecurringCharacter(input): 
    table = {}
    for num in input:
        if num not in table:
            table[num] = 1
        else:
            return num
    return None

print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))
