def getData():
    data = []
    with open("input", "r") as file:
        for line in file:
            line = line.strip()
            data.append(line)

    return data


def main():
    sum = 0
    data = getData()

    print(f"Data: \n{data}")
    print(sum)


if __name__ == "__main__":
    main()
    print("Done")

"""
Sudocode
"""
