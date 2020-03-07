

def length(txt):
    if txt == "":
        return 0
    else:
        return length(txt[1:]) + 1





# Test case

print(length("apple")) # 5

print(length("make")) # 4

print(length("a")) # 1

print(length("")) # 0

