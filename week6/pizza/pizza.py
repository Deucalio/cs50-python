import sys
import csv
from tabulate import tabulate

# table = [["Cheese", "$25.50", "$39.95"], ["1 item", "$27.50", "$41.95"],
#          ["2 items", "$29.50", "$43.95"], ["3 items", "$31.50", "$45.95"],
#          ["Special", "$33.50", "$47.95"]]

# headers=["Sicilian Pizza","Small", "Large"]

# print(tabulate(table, headers, tablefmt="grid"))


if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 2):
    sys.exit("Too many command-line arugments")

csv_file = sys.argv[1]
if not csv_file.endswith(".csv"):
    sys.exit("Not a CSV File")

TABLE = []
HEADERS = []
try:
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        HEADERS = reader.fieldnames
        for row in reader:
            value = list(row.values())
            TABLE.append(value)

    print(tabulate(TABLE, HEADERS, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")

