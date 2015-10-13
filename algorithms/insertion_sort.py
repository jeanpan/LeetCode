def insertionSort(alist):
    n = len(alist)
    for i in range(1, n):
        curvalue = alist[i]
        pos = i

        while pos > 0 and curvalue < alist[pos - 1]:
            alist[pos] = alist[pos - 1]
            pos = pos - 1

        alist[pos] = curvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)