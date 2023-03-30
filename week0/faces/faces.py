def main():
    prompt = input()
    print(convert(prompt))


def convert(string):
    converted = string.replace(":(", "🙁")
    converted = converted.replace(":)", "🙂")
    return converted


main()
