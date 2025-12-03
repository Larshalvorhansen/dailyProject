#!/usr/bin/env python


def is_invalid_id(i):
    """Check if a number can be expressed as a pattern repeated exactly twice"""
    s = str(i)
    length = len(s)

    # Must be even length to be repeated twice
    if length % 2 != 0:
        return False

    middle = length // 2
    return s[:middle] == s[middle:]


def checkRange(start, stop):
    total = 0
    for i in range(int(start), int(stop) + 1):  # Include the endpoint
        if is_invalid_id(i):
            total += i
    return total


def main():
    finalSum = 0
    with open("input", "r") as file:
        content = file.read().strip()
        ranges = content.split(",")

    for range_str in ranges:
        start, end = range_str.split("-")
        finalSum += checkRange(start, end)

    print(f"final sum {finalSum}")


if __name__ == "__main__":
    main()
