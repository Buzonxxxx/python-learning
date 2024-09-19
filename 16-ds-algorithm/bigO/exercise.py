# What is the Big O of the below function? (Hint, you may want to go line by line)
def anotherFunChallenge(input):
    a = 5 #O(1)
    b = 10 #O(1)
    c = 50 #O(1)
    for i in range(len(input)):
        x = i + 1 #O(n)
        y = i + 2 #O(n)
        z = i + 3 #O(n)

    for j in range(len(input)):
        p = j * 2 #O(n)
        q = j * 2 #O(n)
    
    whoAmI = "I don't know" #O(1)

# O(4 + 5n) = O(n)