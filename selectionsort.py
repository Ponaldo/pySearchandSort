def selectionsort():
    lst = []
    n = int(input("Enter the number of elements in your list: "))
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)
    print("Unsorted list: " + str(lst))

    for x in range(0, n):
        findex = x
        for z in range(x + 1, n):
            if lst[z] < lst[findex]:
                findex = z
        (lst[x], lst[findex]) = (lst[findex], lst[x])
    print("Sorted list: " + str(lst))


selectionsort()
