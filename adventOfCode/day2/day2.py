#!/usr/bin/env python
# Kule saker


def check2(i):
    middle = int(len(str(i)) / 2)
    if str(i)[:middle] == str(i)[middle:]:
        return True
    else:
        return False


def check3(i):
    split = int(len(str(i)) / 3)
    if str(i)[:split] == str(i)[split : split * 2] == str(i)[split * 2 :]:
        return True
    else:
        return False


def check5(i):
    split = int(len(str(i)) / 5)
    if (
        str(i)[:split]
        == str(i)[split : split * 2]
        == str(i)[split * 2 : split * 3]
        == str(i)[split * 3 : split * 4]
        == str(i)[split * 4 :]
    ):
        return True
    else:
        return False


def checkRange(start, stop):
    sum = 0
    for i in range(int(start), int(stop)):
        if i < 10:
            sum += 0
        elif len(str(i)) % 2 == 0 and check2(i):
            sum += i
        elif len(str(i)) % 3 == 0 and check3(i):
            sum += i
        elif len(str(i)) % 5 == 0 and check5(i):
            sum += i
        else:
            if len(set(str(i))) == 1:
                sum += i
    return sum


def main():
    lines = []
    finalSum = 0
    with open("input", "r") as file:
        for line in file:
            lines = line.split(",")
    for line in lines:
        finalSum += checkRange(line.split("-")[0], line.split("-")[1])

    print(f"final sum {finalSum}")


if __name__ == "__main__":
    main()
