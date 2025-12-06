"""
for each new line:
    sum += distance between end of first with start of second

final answer = last number - fist number - sum

"""


def getDistance(first, second):
    num1 = int((first.strip()).split("-")[1])
    num2 = int((second.strip()).split("-")[0])
    distance = num2 - num1
    print(f"num1 {num1}, num2 {num2}, distance {distance}")


def main(inn, out):
    with open(inn, "r") as f:
        lines = [line.strip() for line in f]

    for i, line in enumerate(lines):
        getDistance(lines[i - 1], lines[i])

    with open(out, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    inn = "input5.txt"
    out = "input6.txt"
    main(inn, out)
    print("Done")
