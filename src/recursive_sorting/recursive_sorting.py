# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = b = c = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        else:
            merged_arr[c] = arrB[b]
            b += 1
        c += 1

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        a += 1
        c += 1

    while b < len(arrB):
        merged_arr[c] = arrB[b]
        b += 1
        c += 1

    return merged_arr


# arr1 = [3, 4, 6, 7, 9, 10]
# arr4 = [1, 2, 5, 8, 11]

# print(merge(arr1, arr4))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # Your code here

    # merging
    if len(arr) > 1:
        mid = len(arr)//2
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
        arr = merge(lhs, rhs)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
