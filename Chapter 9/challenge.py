def groupByEvenUneven(arr):
    even = []
    uneven = []

    for idx, num in enumerate(arr):
        if num%2 == 0:
            even.append(num)
        else:
            uneven.append(num)

    return even + uneven

testList = [2, 4, 7, 4, 23, 8, 0, 16, 23, 22, 11, 67, 34, 57, 59, 43]

print(groupByEvenUneven(testList))