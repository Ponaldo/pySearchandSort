def mindex():
    lst = []
    n = int(input("Enter the number of elements in your list: "))
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)
    print("List: " + str(lst))
    findex = 0
    cmin = lst[0]
    for x in range(0, n):
        if lst[x] < cmin:
            cmin = lst[x]
            findex = x
    print("minimum is " + str(cmin) + " and the index is " + str(findex))


mindex()