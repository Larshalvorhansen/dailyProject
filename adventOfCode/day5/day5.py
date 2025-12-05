def check(start: int, num: int, stop: int) -> bool:
    if (num >= start) and (num <= stop):
        print(f"{start} < {num} < {stop}\t = true")
        return True
    else:
        print(f"{start} < {num} < {stop}\t = false")
        return False


def main():
    sum = 0

    with open("inputb", "r") as fileb:
        # For all ingredients
        for linen in fileb:
            line = linen.strip()
            print(f"the new line is: {line}")
            # Check ingredient in all ranges
            with open("inputa", "r") as filea:
                flag = False
                for linen in filea:
                    rangee = (linen.strip()).split("-")
                    if check(int(rangee[0]), int(line), int(rangee[1])):
                        print(f"line {line}\t is fresh")
                        flag = True
                        break
                    else:
                        print(f"line {line}\t is spoiled")
                        flag = False
                print("")
                if flag:
                    sum += 1
            filea.close()
    print(f"sum {sum}")


if __name__ == "__main__":
    main()
    print("Done")

"""
Sudocode:

for each number in b:
    check if in any a

runtime: a * b = 1000 * 340
"""
