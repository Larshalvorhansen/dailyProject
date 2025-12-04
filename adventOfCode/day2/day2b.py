def makeList(start, stop):
    with open("output", "w+") as f:
        for i in range(start, stop):
            f.write(str(i))
            f.write("\n")
        print("File written successfully")

    f.close()


def main():
    with open("input", "r") as file:
        for l in file:
            lines = l.split(",")
            for line in lines:
                start = line.split("-")
                end = int(start[1])
                start = int(start[0])
                print(f"start {start} end {end}")
                makeList(start, end)


if __name__ == "__main__":
    main()
