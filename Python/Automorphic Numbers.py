


def is_automorphic(n):
    if str(n ** 2).endswith(str(n)):
        return True
    return False





# Test case

print(is_automorphic(5)) # True

print(is_automorphic(8)) # False

print(is_automorphic(76)) # True
