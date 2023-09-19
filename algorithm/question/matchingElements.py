
# O(n^2)
def matching_elements(l1, l2):
    for ele in l1:
        if ele in l2:
            return True
    return False

# O(m+n)
def better_matchine_elements(l1, l2):
    table = {}
    for ele in l1:
        if ele not in table:
            table[ele] = True
    for ele in l2:
        if ele in table:
            return True
    return False





print(matching_elements(['a','b','c','x'], ['x','y','z']))
print(better_matchine_elements(['a','b','c','x'], ['x','y','z']))