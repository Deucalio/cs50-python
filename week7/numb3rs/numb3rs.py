import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    four_digits = ip.split(".")
    if len(four_digits) != 4:
        return False
    for digit in four_digits:
        if digit.isalpha():
            return False
        try:
            if int(digit) > 255:
                return False
        except ValueError:
            continue
    return True
        


...


if __name__ == "__main__":
    main()
