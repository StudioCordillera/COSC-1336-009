class A:
    # Init.
    def __init__(self, value):
        self.__value = value

    # Two-underscore name.
    __value = 0

# Create the class.
a = A(5)

# [1] Cannot use two-underscore name.
# print('Cannot use two-underscore name', a.__value)

# [2] Must use mangled name.
print('Must use mangled name', a._A__value)


