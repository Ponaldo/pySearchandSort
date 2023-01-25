def linear():
    userarr = []
    n = int(input("Enter the number of elements in your list: "))
    found = False
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        userarr.append(ele)

    f = int(input("Enter the number you want to find in the list: "))

    for i in range(0, n):
        if f == userarr[i]:
            print("The number has been found. It is " + str(userarr[i]))
            found = True
            break

    if not found:
        print("Number not found.")



linear()
