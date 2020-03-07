


def sum_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_numbers(n - 1)




# Test case

print(sum_numbers(5)) # 15

print(sum_numbers(1)) # 1

print(sum_numbers(12)) # 78

