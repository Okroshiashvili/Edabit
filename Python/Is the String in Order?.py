


def is_in_order(txt):
    if list(txt) == sorted(list(txt)):
        return True
    return False





# Test case

print(is_in_order("abc")) # True

print(is_in_order("edabit")) # False

print(is_in_order("123")) # True

print(is_in_order("xyzz")) # True

print(list('abc'))

