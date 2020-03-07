

def convert_cartesian(x, y):
    return [list(i) for i in zip(x,y)]






# Test case

print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0])) # [[1, 5], [5, 8], [3, 9], [3, 1], [4, 0]]

print(convert_cartesian([9, 8, 3], [1, 1, 1])) # [[9, 1], [8, 1], [3, 1]]




