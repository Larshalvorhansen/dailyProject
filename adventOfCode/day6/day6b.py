# import numpy as np


def getData():
    data = []
    with open("input", "r") as file:
        for i, line in enumerate(file):
            line = [line.strip().split(" ")]
            l = line[0]
            # cl = [x for x in l if x]
            if i != 4:
                l2 = [int(x) for x in l]
            else:
                l2 = l
            print(l2)
            data.append(l2)

    return data


def main():
    sum = 0
    data = getData()

    tdata = [list(row) for row in zip(*data)]
    for i, row in enumerate(tdata):
        # for j, col in enumerate(row):
        if row[-1] == "+":
            ksum = 0
            for k in row:
                if type(k) == int:
                    ksum += k
            print(ksum)
            sum += ksum
        elif row[-1] == "*":
            ksum = 1
            for k in row:
                if type(k) == int:
                    ksum = ksum * k
            print(ksum)
            sum += ksum
            # print(f"i {i} j {j} col {col}")

    print(f"data: \n {tdata}")
    print(f"sum {sum}")


if __name__ == "__main__":
    main()
    print("Done")

"""
Sudocode

make array of input
transpose array
for line in array:
    get final element (* or +)
        if *:
            multiply all elements
            add to sum
        if +:
            add all elements
            add to sum
print(sum)
"""
