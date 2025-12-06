def getData():
    data = []
    with open("input", "r") as file:
        for line in file:
            line = [int(line.strip().split("-")[0]), int(line.strip().split("-")[1])]
            data.append(line)

    return data


def main():
    sum = 0
    data = getData()

    print(sum)


if __name__ == "__main__":
    main()
    print("Done")

"""
Sudocode
"""
