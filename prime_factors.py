def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(num):
    new = []
    for x in range(1, num):
        if num % x == 0 and prime(x):
            new.append(x)
    return new


print(prime_factors(24))  # => [2, 3]
print(prime_factors(60))  # => [2, 3, 5]
