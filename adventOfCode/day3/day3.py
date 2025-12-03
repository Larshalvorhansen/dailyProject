def maxJolt(num):
    lastDig = 0
    firstDig = 0
    digits = list(map(int, str(int(num))))
    biggest = 1
    pos = -1
    for i, digit in enumerate(digits):
        if digit >= biggest:
            biggest = digit
            pos = i
    if pos == len(digits):
        lastDig = biggest
        digits.pop()
        firstDig = max(digits)
        return firstDig * 10 + lastDig
    else:
        firstDig = biggest
        del digits[: pos + 1]
        digits.insert(0, 0)
        print(f"leftover digs {digits}")
        lastDig = max(digits)
        return firstDig * 10 + lastDig


def main():
    sum = 0
    with open("test", "r") as file:
        for line in file:
            print(f"{line.strip()}")
            num = maxJolt(line.strip())
            print(f"line max {num}")
            sum += num
    print(sum)


if __name__ == "__main__":
    main()

"""
ta det første høyeste tall
Har det tall bak seg?
ja -> lagre tallet og velg det høyeste tallet etter det tallet
nei -> lagre tallet som siste tall og velg det høyeste før.
"""
