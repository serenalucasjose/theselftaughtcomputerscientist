import random

# Generate mock data
NUMS_MAX = 10

numList = []
for i in range(NUMS_MAX):
    numList.append(round(random.uniform(0, 1), 3))

# Bucket sort
def bucketSort(array):
    n = 10

    if len(array) <= 0:
        return False
    
    # Create n empty arrays
    buckets = [[]] * n
    # Put items in buckets
    for num in array:
        bIdx = int(num * n)
        buckets[bIdx].append(num)
    # Sort buckets
    for i in range(n):
        buckets[i] = sorted(buckets[i])
    # Gather buckets
    j = 0
    for bIdx in range(n):
        for j in range(len(buckets[bIdx])-1):
            array[j] = buckets[bIdx][j]
            j+=1

    return array

print(bucketSort(numList))    