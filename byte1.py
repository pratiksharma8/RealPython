def median(arr1, arr2):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr1)):
        sum1 += arr1[i]
        avg1 = sum1/len(arr1)

    for j in range(len(arr2)):
        sum2 += arr2[j]
        avg2 = sum2 / len(arr2)

    print(avg1 + avg2 / 2)


median([1, 3, 5], [2, 4, 6])
