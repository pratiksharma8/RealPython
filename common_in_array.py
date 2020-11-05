def common(arr1, arr2):
    same = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                same.append(arr1[i])
    print(same)


common([1, 2, 3, 4, 5, 6], [3, 4, 6, 7, 8, 9])
