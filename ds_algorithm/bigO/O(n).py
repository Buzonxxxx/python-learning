import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]
def find_nemo(list):
    t0 = time.time()
    for i in range(0,len(list)):
        if list[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')

find_nemo(nemo) # O(n) -> Linear Time
find_nemo(everyone)
find_nemo(large)

def funchallenge(input):
    a = 10 #O(1)
    a = a + 3 #O(1)
    for i in range(len(input)): #O(n)
        stranger = True #O(n)
        a += 1 #O(n)
    return a #O(1)

funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)

# O(n)