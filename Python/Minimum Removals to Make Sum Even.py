


def minimum_removals(lst):
    if sum(lst) % 2 == 0:
        return 0
    else:
        return 1 + minimum_removals(lst[1:])





# Test case

print(minimum_removals([1, 2, 3, 4, 5])) # 1

print(minimum_removals([5, 7, 9, 11])) # 0

print(minimum_removals([5, 7, 9, 12])) # 1

