def returnHigh(it: int):
    _num = list(str(it))
    _list = []
    for i in range(len(_num)):
        newlist = _num[:i] + _num[i + 1 :]
        _list.append(newlist)
    _result = []
    for i in _list:
        result = "".join(i)
        _result.append(int(result))
    return max(_result)


def main():
    sum = 0
    with open("input", "r") as file:
        for line in file:
            it = int(line.strip())
            while len(str(it)) > 12:
                it = returnHigh(it)
                print(it)
            sum += it
    print(sum)


if __name__ == "__main__":
    main()
