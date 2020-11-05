def odd_even(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")


odd_even(30)
