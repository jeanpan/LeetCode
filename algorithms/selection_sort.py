def selectionSort(alist):
    for r in range(len(alist) - 1, 0, -1):
        m = 0
        for i in range(r):
            if alist[i] > alist[m]:
                m = i
        alist[m], alist[r] = alist[r], alist[m]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
