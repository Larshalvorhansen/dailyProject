def returnHigh(it: int):
    # it = str(it)
    _num = list(map(str, it))
    _list = []
    for i, item in enumerate(_num):
        newlist = _num[:i] + _num[i + 1 :]
        _list.append(newlist)
        break
    _result = []
    for i in _list:
        result = "".join(map(str, i))
        _result.append(int(result))
    it = max(_list)
    return it


def main():
    with open("small", "r") as file:
        for line in file:
            it = int(line.strip())

    for i in range(10):
        it2 = returnHigh(it)
        it = returnHigh(it2)


if __name__ == "__main__":
    main()
