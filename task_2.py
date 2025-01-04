def binary_search_fractional(lst, search_value):
    low = 0
    high = len(lst) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if search_value == lst[mid]:
            return (steps, lst[mid])
        elif lst[mid] < search_value:
            low = mid + 1
        else:
            high = mid - 1
    return (steps, lst[low])


print(
    binary_search_fractional([1.1, 1.3, 4.5, 7.2, 8.3, 9.6, 11.2], 8),
)
