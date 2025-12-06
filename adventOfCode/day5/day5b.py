def checkOverlap(range1: str, range2: str):
    min1 = (range1.strip()).split("-")[0]
    max1 = (range1.strip()).split("-")[1]
    min2 = (range2.strip()).split("-")[0]
    max2 = (range2.strip()).split("-")[1]

    if ((min1 <= max2) and (min2 <= max1)) or ((min2 <= max1) and (min1 <= max2)):
        newMin = min(min1, min2)
        newMax = max(max1, max1)
        return (int(newMin.strip()), int(newMax.strip()))
    else:
        return (1, 1)


def removeInsiders(range1: str, range2: str):
    min1 = (range1.strip()).split("-")[0]
    max1 = (range1.strip()).split("-")[1]
    min2 = (range2.strip()).split("-")[0]
    max2 = (range2.strip()).split("-")[1]

    if ((min1 >= min2) and (max1 <= max2)) or ((min2 >= min1) and (max2 <= max1)):
        newMin = min(min1, min2)
        newMax = max(max1, max1)
        return (int(newMin.strip()), int(newMax.strip()))
    else:
        return (1, 1)


def replaceRanges(pos1, pos2, newRange, inn, out):
    newRange = f"{newRange[0]}-{newRange[1]}\n"

    with open(inn, "r") as file:
        lines = file.readlines()

    lines[pos1] = newRange
    del lines[pos2]
    print(f"lines[pos1] {newRange}")
    print(f"pos2 {pos2}")

    with open(out, "w") as file:
        file.writelines(lines)


def sortLines(inn, out):
    with open(inn, "r") as f:
        lines = [line.strip() for line in f]

    lines.sort(key=lambda x: int(x.split("-")[0]))

    with open(out, "w") as f:
        for line in lines:
            f.write(line + "\n")


def main(inn, out):
    with open(inn, "r") as file1:
        for pos1, range1 in enumerate(file1):
            with open(inn, "r") as file2:
                for pos2, range2 in enumerate(file2):
                    if range1 != range2:  # Skip identical rangecheck
                        newRange = removeInsiders(range1, range2)
                        print(f"range1: {range1.strip()}, range2: {range2.strip()}")
                        replaceRanges(pos1, pos2, newRange, inn, out)


if __name__ == "__main__":
    for i in range(100):
        inn = "input.txt"
        out = "input2.txt"
        main(inn, out)
        inn = "input2.txt"
        out = "input3.txt"
        main(inn, out)
        inn = "input3.txt"
        out = "input4.txt"
        main(inn, out)
        inn = "input4.txt"
        out = "input.txt"
        main(inn, out)
    sortLines("input4.txt", "input5.txt")
    print("Done")

"""
Sudocode:

def checkOverlap(min1, min2, max1, max2):
    if (min1 <= max2) or (min2 <= max1):
        newMin = min(min1, min2)
        newMax = max(max1, max1)
        return(newMin, newMax)
    else: 
        return(1,1)

def replaceRanges(pos1, pos2, newRange):
    with open ...
    remove pos1, pos2
    append newRange

for each range:
    for each other range:
        if checkOverlap() != (1,1):
            replaceRanges(range1pos, range2pos, newRange)

"""
