

def factorial(Z):
    if Z <= 1:
        return 1
    else:
        return Z * factorial(Z - 1)






# Test case

print(factorial(4)) # 24

print(factorial(0)) # 1

print(factorial(9)) # 362880




