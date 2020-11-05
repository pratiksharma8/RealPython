def o_words(sentence):
    s = sentence.split(" ")
    s = [x for x in s if "o" in x]
    print(s)
o_words("How did you do that?") #=> ["How", "you", "do"]