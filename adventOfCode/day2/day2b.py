def makeList(start, stop):
    with open("output", "a") as f:
        for i in range(start, stop + 1):
            f.write(str(i))
            f.write("\n")
        # print("File written successfully")
    f.close()


def check(line, length):
    digs = list(map(int, line.strip()))

    if length == 1:
        return False

    if length % 2 == 0:
        half = int(length * 0.5)
        if digs[0:half] == digs[half:]:
            return True

    if length % 3 == 0:
        third = int(length / 3)
        if digs[0:third] == digs[third : 2 * third] == digs[2 * third :]:
            return True

    if length % 5 == 0:
        fifth = int(length / 5)
        if (
            digs[0:fifth]
            == digs[fifth : 2 * fifth]
            == digs[2 * fifth : 3 * fifth]
            == digs[3 * fifth : 4 * fifth]
            == digs[4 * fifth :]
        ):
            return True

    sorted_digs = sorted(digs)
    if sorted_digs[0] == sorted_digs[-1]:
        return True

    return False


def main():
    sum = 0

    with open("input", "r") as file:
        for l in file:
            lines = l.split(",")
            for line in lines:
                print(line)
                start = line.split("-")
                try:
                    end = int(start[1])
                    start = int(start[0])
                except:
                    pass
                # print(f"start {start} end {end}")
                makeList(start, end)

    with open("output", "r") as file:
        for line in file:
            length = len(str(line.strip()))
            if check(line, length):
                print(f"len {length}, {line.strip()}")
                sum += int(line.strip())
        print(sum)


if __name__ == "__main__":
    main()
