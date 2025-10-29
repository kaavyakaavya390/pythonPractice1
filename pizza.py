import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(rows, headers="keys", tablefmt="grid"))


main()
