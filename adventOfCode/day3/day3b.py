def mStrip(line):
    nums = list(map(int, str(line.strip())))
    while True:
        print("")
        print("")
        for i, num in enumerate(nums):
            if num == min(nums) and num <= nums[i + 1]:
                nums.pop(i)
            print(nums)
            print(len(nums))
            # print(len(nums))
            if len(nums) == 12:
                # print(f"nums {nums}")
                # print(f"line {line}")
                a = "".join(map(str, nums))
                # print(f"a {a}")
                return a


def main():
    sum = 0
    with open("small", "r") as file:
        for line in file:
            # print(f"int(mStrip(line)) {int(mStrip(line))}")
            sum += int(mStrip(line))
            # print("")

    print(sum)
    print(len(str(sum)))


if __name__ == "__main__":
    main()
