
while True:
    try:
        fraction = input("Fraction: ").split("/")
        x, y = fraction
        x = int(x)
        y = int(y)
        percentage = str(round((x / y) * 100)) + "%"
        int_percentage = int(percentage.replace("%", ""))
        if (int_percentage >= 98):
             if (int_percentage > 100):
                continue
             else:
                 percentage = "F"
        elif (int_percentage <= 5):
            percentage = "E"
        print(percentage)
        break
    except (ValueError, ZeroDivisionError):
        pass
