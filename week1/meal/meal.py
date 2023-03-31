def main():
    time = input("What time is it? ")
    time = convert(time)
    if (7 <= time <= 8):
        print("breakfast time")
    elif (12 <= time <= 13):
        print("lunch time")
    elif (18 <= time <= 19):
        print("dinner time")



def convert(time):
    first_digit, last_digit = time.split(":")
    last_digit = "6" if (int(last_digit)) >= 31 else ("25" if (int(last_digit)) == 15 else ("00" if (int(last_digit)) == 00 else "5")  )
    return (float(first_digit + "." + last_digit))


if __name__ == "__main__":
    main()
