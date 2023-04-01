def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # if all letters are text of string, then that's valid
    # d = ""
    # if max_6_characters(s):
    #     for let in s:
    #         if (let.isnumeric()):
    #             d += let
    # if (len(d) == 0):
    #     return True

    if (starts_with_two_letters(s) and max_6_characters(s) and numbers_at_end(s) and last_check(s)):
        return True
    else:
        return False


# starts with atleast two letters
def starts_with_two_letters(text):
    return text[0:2].isalpha()

# maximum of 6 characters and a minimum of 2 characters.


def max_6_characters(text):
    return 2 <= len(text) <= 6


# numebers must be at the very end. The first number used cannot be a 0
def numbers_at_end(text):
    return ( text[-2:].isnumeric() or text[-2:].isalpha() ) and (True if text.find("0") == -1 else text[text.find("0")-1].isalpha() == False)

# ensure no periods, spaces, or punctuation marks are used


def last_check(text):
    return text.strip() == text and (text.find(",") == -1 and text.find("'") == -1) and text.find(".") == -1


main()
