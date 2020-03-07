


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)




# Test case

print(gcd(10, 20)) # 10

print(gcd(1, 3)) # 1

print(gcd(5, 7)) # 1

print(gcd(2, 6)) # 2 



