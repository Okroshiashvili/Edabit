


def unique_sort(lst):
    return sorted(list(set(lst)))



# Test case

print(unique_sort([1, 2, 4, 3])) # [1, 2, 3, 4]

print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])) # [1, 2, 3, 4]

print(unique_sort([6, 7, 3, 2, 1])) # [1, 2, 3, 6, 7]


