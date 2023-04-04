import inflect
p = inflect.engine()


def print_names(names):

    result = p.join(tuple(names))
    print(f"Adieu, adieu, to {result}")


names = []
while True:
    try:
        name = input("Name: ").strip()
        if (name == ""):
            print_names(names)
            break
        names.append(name)
    except EOFError:
        print_names(names)
        break
