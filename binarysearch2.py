import math


def endf(x, y):
    return math.ceil(((x+y)-1) / 2)



def bisearch2():
    lst = []
    found = False
    n = int(input("Enter the number of elements in your list: "))
    start = 0
    end = n
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)

    print("Unsorted list: " + str(lst))
    lst.sort()
    print("Sorted list: " + str(lst))
    findnum = int(input("Which number do you want to find?: "))

    while start < end-1:
        print(str(x) + " is x")
        mid = endf(start, end)
        if findnum > lst[mid]:
            start = mid
            print("done " + str(start) + " " + str(end))
        elif findnum == lst[mid]:
            found = True
            break
        elif findnum < lst[mid]:
            end = mid
            print("done 2 " + str(start) + " " + str(end))

    if not found:
        print("Number not found :(")
    else:
        print("The number " + str(findnum) + " was found! very nice")


bisearch2()
