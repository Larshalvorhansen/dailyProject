def getData():
    data = []
    with open("input", "r") as file:
        for line in file:
            line = line.strip()
            line = list(map(int, line.split(",")))
            data.append(line)

    return data


def getSquareSize(p1, p2):
    size = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    temp = []
    temp.append(p1)
    temp.append(p2)
    return size


def main():
    sum = 0
    data = getData()
    print(data)

    temp = [getSquareSize(i, j) for i in data for j in data]
    print(temp)

    print(max(temp))


if __name__ == "__main__":
    main()
    print("Done")

"""
Answer is around: 428556315
"""
