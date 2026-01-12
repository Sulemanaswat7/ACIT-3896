def linear_search(needle, haystack):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return None

print(linear_search(8, [6, 2, 8, 4]))
print(linear_search(4, [6, 2, 8, 4]))
print(linear_search(5, [6, 2, 8, 4]))



def binary_search(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = (left + right) // 2

        if haystack[mid] == needle:
            return mid
        elif needle < haystack[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None

print(binary_search(8, [2, 4, 6, 8]))
print(binary_search(2, [2, 4, 6, 8]))
print(binary_search(1, [2, 4, 6, 8]))
print(binary_search(99, [2, 4, 6, 8]))
print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))
print(binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))

















