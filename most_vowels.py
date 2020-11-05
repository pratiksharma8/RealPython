def vowel_count(word):
    count = 0
    vowels = 'aeiou'
    for x in word.lower():
        if x in vowels:
            count += 1
    return count


def most_vowels(sentence):
    counts = {}
    words = sentence.split()
    for x in words:
        counts[x] = vowel_count(x)
    p = [v for k, v in counts.items()]
    s = [k for k, v in counts.items() if v == max(p)]
    print("".join(s))


most_vowels("what a wonderful world life")  # => "wonderful"
