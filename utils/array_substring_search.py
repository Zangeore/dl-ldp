def array_substring_search(array: list, substring: str):
    for i in range(len(array)):
        if substring in array[i]:
            return i
    return -1
