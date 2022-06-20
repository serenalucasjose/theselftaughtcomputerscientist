from bisect import bisect_left

words_list = [
    'aberrant',
    'bite-sized',
    'boat',
    'decorous',
    'devilish',
    'drawer',
    'erratic',
    'even',
    'geese',
    'joke',
    'leer',
    'like',
    'pest',
    'pets', 
    'produce', 
    'quack', 
    'rapid', 
    'recognize', 
    'sheet', 
    'silky', 
    'submit', 
    'tank', 
    'tawdry', 
    'tree', 
    'whispering'
]

# Using built in function
def search_binary_bisect(list, o):
    idx = bisect_left(list, o)
    if idx <= len(list) - 1 and list[idx] == o:
        return True
    return False

first_result = search_binary_bisect(words_list, 'even') # True

# Using custom binary search fn
def search_binary_custom(a_list, word):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if (a_list[mid] == word):
            return True
        else: 
            if ord(word[0]) < ord(a_list[mid][0]):
                last = mid - 1
            else:
                first = mid + 1
    return False

second_result = search_binary_custom(words_list, 'geese')

print('second_result', second_result)