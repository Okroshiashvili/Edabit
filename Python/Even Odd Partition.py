

def even_odd_partition(lst):
    return [[i for i in lst if i % 2 == 0],
            [j for j in lst if j % 2 == 1]]




# Test case

print(even_odd_partition([5, 8, 9, 2, 0])) # [[8, 2, 0], [5, 9]]

print(even_odd_partition([1, 0, 1, 0, 1, 0])) # [[0, 0, 0], [1, 1, 1]]

print(even_odd_partition([1, 3, 5, 7, 9])) # [[], [1, 3, 5, 7, 9]]

print(even_odd_partition([])) # [[], []]

