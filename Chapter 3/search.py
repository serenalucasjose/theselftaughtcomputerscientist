from bisect import bisect_left

unordered_list =  [1, 22, 15, 16, 6, 54, 2, 76, 11, 13]
ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def linear_search(a_list, n):
    for i in a_list:
        if (i == n):
            return True
    return False

def binary_search_custom(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid =  (first + last) // 2
        if a_list[mid] == n:
            return True
        else: 
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

def binary_search_builtin(a_list, n):
    index = bisect_left(a_list, n)
    if index <= len(a_list) - 1 and a_list[index] == n:
        return True
    return False

print("Linear search (custom): ", linear_search(unordered_list, 9))
print("Linear search (built in): ", 6 in unordered_list)
print("Binary search (custom): ", binary_search_custom(ordered_list, 5))
print("Binary search (built in): ", binary_search_builtin(ordered_list, 11))
