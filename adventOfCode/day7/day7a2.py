def getData():
    data = []
    with open("exampleinput", "r") as file:
        for line in file:
            line = line.strip()
            data.append(line)

    return data


def generateNext():
    pass


def main():
    sum = 0
    data = getData()

    listlist = []
    for i, line in enumerate(data):
        line = [ch for ch in line]
        listlist.append(line)

    print(sum)


if __name__ == "__main__":
    main()
    print("Done")

"""
Sudocode

splt = 0

generate next line form previous line:
generateNext(cp, c)
    new = []
    if c[i] == ^ and cp[i] == | : 
        splt += 1
        cn[i] = .
        c[i-1] = |
        c[i+1] = |
        cn[i+1] = |
        cn[i+1] = |
    new.append[c]
    new.append[cn]
    return new
"""
