def bubbles():
    lst = []
    n = int(input("Enter the number of elements in your list: "))
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)
    print("Unsorted list: " + str(lst))

    for y in range(0, n):
        for z in range(0, n-1):
            if lst[z+1] < lst[z]:
                b = lst[z]
                lst[z] = lst[z+1]
                lst[z+1] = b


    print("sorted: " + str(lst))


bubbles()
