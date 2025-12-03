for i in range(1, 1000):
    for j in range(2, len(str(i))):
        print(f"i {i}  j {j}")
        if len(str(i)) % j == 0:
            print(f"heihei i {i}  j {j}")
