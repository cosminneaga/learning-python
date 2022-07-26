# MRO - Method Resolution Order

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


#        A
#      /   \
#     /     \
#    B       C
#     \     /
#      \   /
#        D


print(D.num)
print()
print(D.mro())
