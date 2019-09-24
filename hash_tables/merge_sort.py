def merge(left, right, index):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][1][index] <= right[j][1][index]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result = result + left[i:] + right[j:]
    return result

def merge_sort(array, index):
    if len(array) >= 2:
        left = merge_sort(array[:len(array) // 2],index)
        right = merge_sort(array[len(array) // 2:], index)
        array = merge(left, right, index)
    return array