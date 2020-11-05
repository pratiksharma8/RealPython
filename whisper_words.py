def whisper_words(words):
    new = [x.lower() + '...' for x in words]
    print(" ".join(new))


whisper_words(["KEEP", "The", "NOISE", "down"])  # => keep... the... noise... down...
