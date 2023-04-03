months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def valid_month(m):
    # try converting month into an int
    try:
        month = int(m)
        if (month <= 0 or month > 12):
            return False
        return True
    # must be string if can't be converted into integer
    except:
        if (m not in months_list):
            return False
        return True


def valid_day(d):
    try:
        day = int(d)
        if (day <= 0 or day > 31):
            return False
        return True
    except (ValueError):
        return False


while True:
    try:
        # accepts date in AD (mm-dd-yy)
        date = input("Date: ")
        invalid_month = False if date.find("/") == -1 else (True if date[date.find("/")-1].isnumeric() == False else False)
        if (invalid_month):
            continue
        date = date.split(" ") if date.find(",") != -1 else date.split("/")
        month, day, year = date
        month = month.strip()
        day = day.strip()
        year = year.strip()
        day = day.replace(",", "").strip()
        if (valid_month(month) and valid_day(day)):
            day = f"0{day}" if len(day) == 1 else day
            month = f"0{month.strip()}" if len(month) == 1 else month.strip()
            if (len(month) > 3):
                month = "0" + str(months_list.index(month)+1) if len(
                    str(months_list.index(month)+1)) == 1 else months_list.index(month)+1
                print(f"{year}-{month}-{day}")
                break

            print(f"{year}-{month}-{day}")
            break

    except ValueError:
        pass
