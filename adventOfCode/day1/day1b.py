#!/usr/bin/env python
# Kule saker


def calPos(input: str) -> int:
    sign = 0
    if input[0] == "L":
        sign = -1
    elif input[0] == "R":
        sign = 1
    return sign


def addPos(input: str) -> int:
    sign = calPos(input)
    return sign * int(input[1:])


def main():
    sum = 50
    count = 0
    with open("input", "r") as file:
        for line in file:
            temp = addPos(line.strip())
            for i in range(abs(temp)):
                if temp < 0:
                    sign = -1
                else:
                    sign = 1
                sum += sign
                sum = sum % 100
                # print(f"addPos {addPos(line.strip())}")
                # print(f"sum {sum}")
                if sum == 0:
                    count += 1
                    # print(f"count: {count}")
    print(count)


# 2971

if __name__ == "__main__":
    main()
