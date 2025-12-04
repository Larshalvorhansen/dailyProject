import numpy as np


def check(lineA, lineB, lineC, j, i):
    if sum(lineB) == 0:
        return False
    object = lineB[j]
    nums = [
        lineA[j - 1],
        lineA[j],
        lineA[j + 1],
        lineB[j - 1],
        lineB[j + 1],
        lineC[j - 1],
        lineC[j],
        lineC[j + 1],
    ]
    if j > 5 and i == -1:
        print(lineA)
        print(lineB)
        print(lineC)
        print(j)
        print(sum(nums))
        print(nums)
        print("")
    if sum(nums) < 4 and object == 1:
        # print("yes")
        return True
    else:
        # print("no")
        return False


def main():
    size = 137
    grid = []
    # print(grid)
    with open("input", "r") as file:
        grid = [line for line in file]

    for i, line in enumerate(grid):
        grid[i] = line.strip()

    for i, line in enumerate(grid):
        grid[i] = line.replace("@", "1")

    for i, line in enumerate(grid):
        grid[i] = line.replace(".", "0")

    for i, line in enumerate(grid):
        grid[i] = list(map(int, str(line)))

    for i, line in enumerate(grid):
        grid[i].append(0)
        grid[i].insert(0, 0)

    print(grid)

    removed = []
    while True:
        c = 0

        solGrid = np.zeros((size + 1, size + 1))

        for i in range(0, size + 1):
            for j in range(size + 1):
                if check(grid[i - 1], grid[i], grid[i + 1], j, i):
                    c += 1
                    solGrid[i][j] = 1
                    grid[i][j] = 0
        print(solGrid)
        print(c)
        removed.append(c)
        print(removed)
        print(grid)

        if c == 0:
            break

    print(sum(removed))


if __name__ == "__main__":
    main()

# 1360 not correct
# 1359 not correct
# 2191 is too high
# 2328 is too high
