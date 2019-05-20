# Q1
passMath = {"Tom", "John", "Mary", "Jimmy", "Summy", "Amy"}
passEnglish = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}

# pass math only
print(passMath - passEnglish)

# pass english only
print(passEnglish - passMath)

# pass both
print(passMath & passEnglish)

# all students
print(passMath | passEnglish)

# Q2
grades = {
    "Tom": [80, 100, 90, 95],
    "John": [100, 93, 75, 80]
}

avgTom = float(sum(grades["Tom"])) / len(grades["Tom"])
avgJohn = float(sum(grades["John"])) / len(grades["John"])

print("Tom\'s average grade is: {}".format(avgTom))
print("John\'s average grade is: {}".format(avgJohn))
