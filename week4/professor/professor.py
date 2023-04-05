from random import randint


def main():
    level = get_level()

    counter = 0
    score = 0
    while counter != 10:
        x, y = generate_integer(level), generate_integer(level)
        counter += 1
        tries = 0
        while (tries != 3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if (answer != x+y):
                    if (tries == 2):
                        print(f"{x} + {y} = {x+y}")
                        break
                    tries += 1
                    print("EEE")
                    continue
                else:
                    if (tries == 0):
                        score += 1
                        break
                    break
            except ValueError:
                if (tries == 2):
                    print(f"{x} + {y} = {x+y}")
                    break
                print("EEE")
                tries += 1
                continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (1 <= level <= 3):
                return level
        except ValueError:
            continue


def generate_integer(level):
    if (level == 1):
        return randint(0, 9)
    elif (level == 2):
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()
