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

    for k in range(10):
        for i in range(len(data)):
            for j in range(len(data)):
                # print(f"i {i}, j {j}")
                if i != j:
                    if (
                        ((data[i][0] <= data[j][1]) and (data[i][1] >= data[j][0]))
                        or (data[i][0] >= data[j][0])
                        and (data[i][1] <= data[j][1])
                    ):
                        small = min(data[i][0], data[j][0])
                        large = max(data[i][1], data[j][1])
                        data[i] = [small, large]
                        data[j] = [0, -1]
    data = sorted(data, key=lambda x: x[0])
    for i in range(len(data)):
        if data[i] != [0, 0]:
            print(data[i])
            sum += abs(data[i][0] - data[i][1]) + 1
            print(abs(data[i][0] - data[i][1]) + 1)
    print(sum)


if __name__ == "__main__":
    main()
    print("Done")

"""
answer = sumOfRangeSizes - totalRange
smallest: 50395470158
biggest: 562097848259759
totalRange: 562047452789601
sumOfRangeSizes: 366374706298377
totalBadInRange: 195672746491224

366374706298659
totalGood: totalRange - totalBadInRange = 562047452789601 - 195672746491224 = 366374706298377

"""
