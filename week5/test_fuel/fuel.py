def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print (gauge(percentage))


def convert(fraction):
    # expects a str in X/Y format as input
    x, y = fraction.split("/")

    if y == "0":
        raise ZeroDivisionError
    if not x.isnumeric() or not y.isnumeric():
        raise ValueError
    if (int(x) > int(y)):
        raise ValueError

    x = int(x)
    y = int(y)
    return (round((x/y)*100))


def gauge(percentage):
    if (percentage <= 1):
        return "E"
    elif (percentage >= 99):
        return "F"
    else:
        return F"{percentage}%"

if __name__ == "__main__":
    main()
