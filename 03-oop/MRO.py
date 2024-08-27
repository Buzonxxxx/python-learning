# MRO - Method Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass


print(D.num) # 1

print(D.mro())


#    A
#   /  \
#  /    \
# B      C
#  \    /
#   \  /
#     D

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

#    object
#   /  |   \
#  /   |    \
# X    Y     Z
#  \  / \   /
#   A     B
#    \   /
#      M

# DFS: Depth First Search
print(M.__mro__) # M -> B -> A -> X -> Y -> Z -> object

