def main():
    print(convert(input("Hours: ")))
# works well for am


def format_time(time, abbr):
    if time.isnumeric():
        if len(time) == 1:
            time = f"0{time}:00" if abbr == "AM" else f'{int(time)+12}:00'
            return time
        time = f'{(int(time)+12)}:00' if abbr == "PM" else f'{time}:00'
        if time == "12:00":
            return "00:00"
        if time == "24:00":
            return "12:00"
        return time
    time = time.split(":")
    if int(time[1]) >= 60:
        raise ValueError
    if len(time[0]) == 1:
        time = f'0{time[0]}:{time[1]}' if abbr == "AM" else f'{int(time[0])+12}:{time[1]}'
        return time
    time = f'{time[0]}:{time[1]}' if abbr == "AM" else f'{int(time[0])+12}:{time[1]}'
    if time == ("24:00"):
        return "12:00"
    if time == "12:00" and abbr == "AM":
        return "00:00"
    return time


def convert(s):
    split_str = s.split(" ")
    if "-" in split_str:
        raise ValueError
    time_1, abbr_1 = split_str[0:2]
    time_2, abbr_2 = split_str[3:]
    return f'{format_time(time_1, abbr_1)} to {format_time(time_2,abbr_2)}'


if __name__ == "__main__":
    main()
