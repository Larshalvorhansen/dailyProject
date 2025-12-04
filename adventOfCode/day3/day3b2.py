def getLargest(next):
    next = str(next)
    lineList = list(map(int, next))
    listlist = []
    for i, item in enumerate(lineList):
        newlist = lineList[:i] + lineList[i + 1 :]
        listlist.append(newlist)
        break
    resultlist = []
    for i in listlist:
        result = "".join(map(str, i))
        resultlist.append(int(result))
    print(listlist)
    next = max(listlist)
    return next


def main():
    with open("small", "r") as file:
        for line in file:
            print(line)
            lineList = list(map(int, line.strip()))
            listlist = []
            for i, item in enumerate(lineList):
                newlist = lineList[:i] + lineList[i + 1 :]
                listlist.append(newlist)
            break
        resultlist = []
        for i in listlist:
            result = "".join(map(str, i))
            resultlist.append(int(result))
            print(f"result {result}")
        next = max(resultlist)

        next2 = getLargest(next)
        print(next2)
        next = getLargest(next2)
        print(next)
        next2 = getLargest(next)
        print(next2)
        next = getLargest(next2)
        print(next)
        next2 = getLargest(next)
        print(next2)
        next = getLargest(next2)
        print(next)
        next2 = getLargest(next)
        print(next2)
        next = getLargest(next2)
        print(next)


if __name__ == "__main__":
    main()
