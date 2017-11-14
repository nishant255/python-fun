def isHappy(n):
    numbers = []

    while True:
        str_number = str(n)
        r = 0
        for i in str_number:
            r += (int(i) * int(i))
        if r == 1:
            return True
        elif r in numbers:
            return False
        numbers.append(r)
        n = r


def writeHappyNumber(numbers, filename):
    happynumbers = []
    for n in range(1, numbers):
        if isHappy(n):
            happynumbers.append(n)
    with open(filename, mode='wt', encoding='utf-8') as happy_number_file:
        happy_number_file.write('\n'.join(str(n) for n in happynumbers))
