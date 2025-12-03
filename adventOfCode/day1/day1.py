#!/usr/bin/env python
# Kule saker


def calPos(input: str):
    sign = 0
    if input[0] == "L":
        sign = -1
    elif input[0] == "R":
        sign = 1
    return sign


def addPos(input: str):
    sign = calPos(input)
    return (sign * int(input[1:])) % 100


def main():
    sum = 50
    count = 0
    with open("input", "r") as file:
        for line in file:
            sum += addPos(line.strip())
            sum = sum % 100
            print(f"addPos {addPos(line.strip())}")
            print(f"sum {sum}")

            if sum == 0:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
