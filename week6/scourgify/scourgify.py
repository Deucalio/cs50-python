import sys
import csv

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many command-line arugments")

input_csv_file, output_csv_file = sys.argv[1:]
if not input_csv_file.endswith(".csv"):
    sys.exit("Not a CSV File")

cleaned_output = []
try:
    with open(input_csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(", ")
            house = row["house"]
            cleaned_output.append(
                {"first": first, "last": last, "house": house})

    with open(output_csv_file, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(cleaned_output)


except FileNotFoundError:
    sys.exit(f"Could not read {input_csv_file}")
