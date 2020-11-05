def space_between(number, n):
    out = []
    out1=[]
    for i in range(len(n)):
        if n[i] in number:
            out.append(n[i])
            ls = out.split(",",0)


            # for j in range(len(out)):
            #     if
    print(ls)


space_between('3141592653589793238462643383279',
              ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793'])
