


def reverse(arg):
    if isinstance(arg, bool):
        return not arg
    else:
        return "boolean expected"






# Test case

print(reverse(True)) # False

print(reverse(False)) # True

print(reverse(0)) # "boolean expected"

print(reverse(None)) # "boolean expected"






