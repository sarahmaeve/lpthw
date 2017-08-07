# Selection sort practice

def selectionSort(sortList):
    for i in range(0, len(sortList) - 1 ):
        min = i
        for j in range(i + 1, len(sortList)):
            if sortList[j] < sortList[min]:
                min = j
        if min != i:
            sortList[min], sortList[i] = sortList[i], sortList[min]
    return sortList


my_unsorted = [46, 6, 23, 8, 2, 5]
print(selectionSort(my_unsorted))
