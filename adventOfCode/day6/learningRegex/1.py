import re


def main():
    Text = "2124 123 12 41 25  43 51 4 21 21 31 3 1231 3 21 3 123 12 3 12"
    print(Text)

    match = re.findall(r"\d{1,}", Text)
    print(match)


if __name__ == "__main__":
    main()
