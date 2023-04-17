

def main():
    print(parse(input("HTML: ")))


def get_url(url):
    split_url = url.split(" ")
    for text in split_url:
        if (text.startswith("src")):
            return text[5:-1]


def parse(s):
    if "iframe" not in s:
        return None
    s = get_url(s) if ("title" in s) else s.split("src=")
    if not s[1].endswith("</iframe>"):
        if "youtube" not in s:
            return None
        return f'https://youtu.be/{s.split("embed/")[1]}'
    if "youtube" not in s[1][1:-11]:
        return None
    return f'https://youtu.be/{s[1][1:-11].split("embed/")[1]}'


...


if __name__ == "__main__":
    main()
