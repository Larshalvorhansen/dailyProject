def check5(i):
    split = int(len(str(i)) / 5)
    if (
        str(i)[:split]
        == str(i)[split : split * 2]
        == str(i)[split * 2 : split * 3]
        == str(i)[split * 3 : split * 4]
        == str(i)[split * 4 :]
    ):
        pass
    print(i)
    print(
        f"{str(i)[:split]} {str(i)[split : split * 2]} {str(i)[split * 2 : split * 3]} {str(i)[split * 3 : split * 4]} {str(i)[split * 4 :]}"
    )
    return 0


for i in range(10000, 100000):
    check5(i)
