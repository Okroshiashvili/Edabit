

def sum_recursively(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_recursively(lst[1:])





# Test case

print(sum_recursively([1, 2, 3, 4])) # 10

print(sum_recursively([1, 2])) # 3

print(sum_recursively([1])) # 1

print(sum_recursively([])) # 0



