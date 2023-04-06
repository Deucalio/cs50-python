def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    filterd_list = list(
        filter(lambda v: v.lower() not in ["a", "e", "i", "o", "u"], word))
    return "".join(filterd_list)


if __name__ == "__main__":
    main()
