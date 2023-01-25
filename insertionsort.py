def insertion():
    lst = []
    n = int(input("Enter the number of elements in your list: "))
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)
    print("Unsorted list: " + str(lst))
    for x in range(1, n):
        j = x
        while j > 0 and lst[j-1] > lst[j]:
            b = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = b
            j -= 1
    print("Sorted list: " + str(lst))


insertion()
