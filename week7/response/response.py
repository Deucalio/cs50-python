from validator_collection import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        email = validators.email(s)
        if email:
            return "Valid"
        return "Invalid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
