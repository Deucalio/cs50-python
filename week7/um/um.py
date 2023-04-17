import re


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    split_str = re.findall(r'\w+', s)
    for word in split_str:
        if word.lower() == "um":
            count += 1
    return count


...


if __name__ == "__main__":
    main()
