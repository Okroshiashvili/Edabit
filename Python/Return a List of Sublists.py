


def matrix(x, y, z):
    return [[z] * y] * x




# Test case

print(matrix(3, 2, 3)) # [[3, 3], [3, 3], [3, 3]]

print(matrix(2, 1, "edabit")) # [["edabit"], ["edabit"]]

print(matrix(3, 2, 0)) # [[0, 0], [0, 0], [0, 0]]



