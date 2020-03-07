

def search(lst, item):
    if item in lst:
        return lst.index(item)
    else:
        return -1



# Test case

print(search([1, 2, 3, 4], 3)) # 2

print(search([2, 4, 6, 8, 10], 8)) # 3

print(search([1, 3, 5, 7, 9], 11)) # -1
