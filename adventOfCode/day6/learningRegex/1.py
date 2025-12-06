import re


def main():
    Text = "I have 3 cats and 2 dogs"
    print(Text)

    match = re.findall("\d", Text)
    print(match)


if __name__ == "__main__":
    main()
