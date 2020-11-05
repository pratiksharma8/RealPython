def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(prime(2))  # => true
print(prime(5))  # => true
print(prime(11))  # => true
print(prime(4))  # => false
print(prime(9))  # => false
print(prime(-5))  # => false
