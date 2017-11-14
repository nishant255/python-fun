def digitPyramid():
    k = 0
    count = 0
    count1 = 0
    rows = int(input("Enter number of rows: "))
    i = 1
    while (i <= rows):

        space = 1
        while (space <= rows - i):
            print("  ", end="")
            count += 1
            space += 1

        while k != 2 * i - 1:
            if count <= rows - 1:
                value = i + k
                if value >= 10:
                    value = value - 10
                print(value, " ", end="")
                count += 1
            else:
                count1 += 1
                value = i + k - 2 * count1
                if value >= 10:
                    value = value - 10
                print(value, " ", end="")
            k += 1
        count1 = count = k = 0
        print("\n", end="")
        i += 1
    return
