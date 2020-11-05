def array(arr):
    new = []
    for i in arr:
        if arr[i] % 2 != 0:
            new.append(-1)
        else:
            new.append(arr[i])
    return new


print(array(range(0, 20)))
