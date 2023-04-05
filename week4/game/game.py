import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
        random_number = random.randint(1, level)
        while True:

            guess = int(input("Guess: "))
            if (guess > random_number):
                print("Too large!")
            elif (guess < random_number):
                print("Too small!")
            else:
                print("Just right!")
                break
        break
    except ValueError:
        continue
