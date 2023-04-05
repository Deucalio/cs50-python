from random import randint

counter = 0
score = 0
while counter != 3:
    x, y = randint(1, 6), randint(1, 6)
    counter += 1
    tries = 0
    while (tries != 3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if (answer != x+y):
                tries += 1
                print("EEE")
                continue
            else:
                if (tries == 0):
                    score += 1
                    # counter += 1
                    break
                break
        except ValueError:
            print("EEE")
            if (tries == 3):
                counter += 1
            tries += 1
            continue
    print("VARIABLES: ", (score, counter))
