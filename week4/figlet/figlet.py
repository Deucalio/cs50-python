# import pyfiglet module
import pyfiglet  # type: ignore
import sys


def valid_font(f):
    try:
        pyfiglet.figlet_format("inital test", font=f)
    except:
        sys.exit("Invalid usage")


# expects 2 command-line arguments
if (len(sys.argv) == 3):
    flag, font = sys.argv[1:]
    valid_font(font)
    if flag not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    text = input("Input: ")
    try:
        result = pyfiglet.figlet_format(text, font=font)
    except:
        sys.exit("Invalid usage")
    print(f"Output: {result}")
    sys.exit()
elif (len(sys.argv) == 1):
    text = input("Input: ")
    try:
        result = pyfiglet.figlet_format(text)
    except:
        sys.exit("Invalid usage")
    print(f"Output: {result}")
    sys.exit()

sys.exit("Invalid usage")
