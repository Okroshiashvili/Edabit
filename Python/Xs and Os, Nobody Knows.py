


def XO(txt):
    if (txt.count('x') + txt.count('X'))  == (txt.count('o') + txt.count('O')):
        return True
    return False





# Test case

print(XO("ooxx")) # True

print(XO("xooxx")) # False

print(XO("ooxXm")) # True
# Case insensitive.

print(XO("zpzpzpp")) # True
# Returns True if no x and o.

print(XO("zzoo")) # False

print(XO("")) # True
