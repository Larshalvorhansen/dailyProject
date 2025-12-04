def makeBiggest(line):
    digits = list(map(int, str(int(line))))

    last = digits[-1]
    noTail = digits[:-1]

    bigPos = getBigPos(noTail)
    # if bigPos[1] == len(str(noTail)):
    print(f"bigPos {bigPos}")
    print(noTail)
    print(f"len notail{len(noTail)}")
    if bigPos[1] + 1 == len(noTail):
        print(f"bigPos {bigPos[0]} last {last}")
        return 10 * bigPos[0] + last
    else:
        noHead = digits[bigPos[1] + 1 :]
        bigPos2 = getBigPos(noHead)
        print(f"{noHead}")
        print(f"{bigPos2}")
        return 10 * bigPos[0] + bigPos2[0]


def getBigPos(digits):
    b = 0
    pos = -1
    for i, digit in enumerate(digits):
        if digit > b:
            b = digit
            pos = i
    return (b, pos)


def main():
    sum = 0

    with open("input", "r") as file:
        for line in file:
            sum += makeBiggest(line.strip())
    print(sum)


if __name__ == "__main__":
    main()

"""
ta det første høyeste tall
Har det tall bak seg?
ja -> lagre tallet og velg det høyeste tallet etter det tallet
nei -> lagre tallet som siste tall og velg det høyeste før.
"""
