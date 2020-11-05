def yell_sentence(sent):
    l = sent.split(" ")
    new = ""
    for i in l:
        new += i + "! "
    print(new.upper())


yell_sentence("I have a bad feeling about this")  # => "I! HAVE! A! BAD! FEELING! ABOUT! THIS!"
