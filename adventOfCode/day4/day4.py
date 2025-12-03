def main():
    finalSum = 0
    with open("input", "r") as file:
        content = file.read().strip()
        ranges = content.split(",")

    for range_str in ranges:
        start, end = range_str.split("-")
        finalSum += checkRange(start, end)

    print(f"final sum {finalSum}")


if __name__ == "__main__":
    main()
