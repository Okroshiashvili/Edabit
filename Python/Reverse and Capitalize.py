

def reverse_capitalize(txt):
    return ''.join(list(txt.upper())[::-1])






# Test case

print(reverse_capitalize("abc")) # "CBA"

print(reverse_capitalize("hellothere")) # "EREHTOLLEH"

print(reverse_capitalize("input")) # "TUPNI"


