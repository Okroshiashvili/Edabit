


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)





# Test case

print(factorial(5)) # 120

print(factorial(3)) # 6

print(factorial(1)) # 1

print(factorial(0)) # 1


