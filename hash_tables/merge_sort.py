def merge(left, right, index):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][index] <= right[j][index]:
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

def sort_func(array, sort_by):
    correct_sort = False
    if sort_by == "":
        print("Unsorted table")
        correct_sort = True
    elif sort_by == "code":
        print("Sorted table by hash_code")
        array = merge_sort(array, 0)
        correct_sort = True
    elif sort_by == "cypher":
        print("Sorted table by cypher")
        array = merge_sort(array, 1)
        correct_sort = True
    elif sort_by == "name":
        print("Sorted table by name")
        array = merge_sort(array, 2)
        correct_sort = True
    elif sort_by == "count":
        print("Sorted table by count")
        array = merge_sort(array, 3)
        correct_sort = True
    else:
        print("Wrong data!!!")
    if correct_sort == True:
        for i in array:
            print(i)