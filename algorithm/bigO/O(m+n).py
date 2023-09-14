import time

large1 = ['nemo' for i in range(100000)]
large2 = ['nemo' for i in range(100000)]

def find_nemo(array1, array2):

    t0 = time.time() #O(1)
    for i in range(0,len(array1)): #O(m)
        if array1[i] == 'nemo': #m*O(1)
            print("Found Nemo!!") #k1*O(1) where k1 <= m because this statement will be executed only if the if statement returns True, which can be k1(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1-t0} seconds.') #O(1)

    t0 = time.time() #O(1)
    for i in range(0, len(array2)): #O(n)
        if array2[i] == 'nemo': #n*O(1)
            print("Found Nemo!!") #k2*O(1) where k2 <= m because this statement will be executed only if the if statement returns True, which can be k2(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1 - t0} seconds.') #O(1)

find_nemo(large1, large2)

# O(m + n)