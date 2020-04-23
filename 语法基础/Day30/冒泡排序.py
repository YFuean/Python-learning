def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i, len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j + 1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    list = [34, 28, 68, 38, 54, 20, 100, 543]
    print(bubble_sort(list))
