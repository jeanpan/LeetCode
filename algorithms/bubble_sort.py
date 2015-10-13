def bubbleSort(alist):
    for r in range(len(alist) - 1, 0, -1):
        for i in range(r):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def shortBubbleSort(alist):
    exchange = True
    r = len(alist) - 1
    while r > 0 and exchange:
        exchange = False
        for i in range(r):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        r = r - 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)