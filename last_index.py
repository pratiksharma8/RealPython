def last_index(s, char):
    ind = 0
    for i in range(len(s)):
        if char == s[i]:
            ind = i
    return ind


print(last_index("abca", "a"))  # => 3
print(last_index("mississipi", "i"))  # => 9
print(last_index("octagon", "o"))  # => 5
print(last_index("programming", "m"))  # => 7
print(last_index("programming", "o"))  # => 2
