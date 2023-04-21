from datetime import date, datetime, time
import sys
import inflect
p = inflect.engine()


def main():
    # prompts the user for their date of birth in YYYY-MM-DD format
    date_of_birth = input("Date of Birth: ")
    if len(date_of_birth.split("-")) != 3:
        sys.exit("Invalid date")
    print(print_minutes(date_of_birth))


# given the date of birth(dob), prints how old user is in minutes
def print_minutes(dob, today_date=date(2000, 1, 1)):
    dob = dob.split("-")
    y = dob[0][2:4]
    m, d = dob[1:]

    formatted_date = datetime.strptime(f"{y}/{m}/{d}", "%y/%m/%d")
    date_tuple = formatted_date.timetuple()
    year, month, day = date_tuple[0:3]
    if year >= 2000:
        today_date = date.today()


    days = abs(date(year, month, day) - today_date).days
    minutes = days * 1440
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
