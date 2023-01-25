import math


def endf(x, y):
    return math.ceil(((x+y) - 1) / 2)


def bisearch():
    lst = []
    found = False
    n = int(input("Enter the number of elements in your list: "))
    start = 0
    end = int(n)
    for x in range(0, n):
        ele = int(input("Input element " + str(x) + ": "))
        lst.append(ele)

    print("Unsorted list: " + str(lst))
    lst.sort()
    print("Sorted list: " + str(lst))
    findnum = int(input("Which number do you want to find?: "))

    try:
        for x in range(start, end):
            print(str(x) + " is x")
            if findnum < lst[0]:
                print("got here")
                break
            elif findnum > lst[len(lst) - 1]:
                break
            elif findnum > lst[endf(start, end)]:
                start = endf(start, end)
                print("done " + str(start) + " " + str(end))
            elif findnum == lst[endf(start, end)] or findnum == lst[start] or (findnum == lst[end-1] and end < (len(lst))/(x*2)):
                print("The number " + str(findnum) + " was found! very nice")
                found = True
                break
            elif findnum < lst[endf(start, end)]:
                end = endf(start, end)
                print("done 2 " + str(start) + " " + str(end))

        if not found:
            print("Number not found :(")
    except IndexError:
        print("Number not found :(")


bisearch()
