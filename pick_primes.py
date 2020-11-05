def primes(num):
    if num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


def pick_primes(numbers):
    new = []
    for i in numbers:
        if primes(i):
            new.append(i)
    return new


print(pick_primes([2, 3, 4, 5, 6]))  # => [2, 3, 5]
print(pick_primes([101, 20, 103, 2017]))  # => [101, 103, 2017]
