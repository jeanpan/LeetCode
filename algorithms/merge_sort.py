def mergeSort(alist):
    n = len(alist)
    if (n > 1):
        mid = n // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        # compare left and right then merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
