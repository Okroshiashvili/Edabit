


def count(deck):
    positive = sum([1 for i in deck if i in [2, 3, 4, 5, 6]])
    negative = sum([-1 for i in deck if i in [10, 'J', 'Q', 'K', 'A']])

    return positive + negative


# Test case

print(count([5, 9, 10, 3, "J", "A", 4, 8, 5])) # 1

print(count(["A", "A", "K", "Q", "Q", "J"])) # -6

print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7])) # 5




"""

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1

"""

