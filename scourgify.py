import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)
            students= list(reader)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w+", newline="") as outfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            last, first = student['name'].split(", ")
            house = student["house"]
            writer.writerow({"first": first, "last": last, "house": house})
        outfile.seek(0)
        reader2=csv.DictReader(outfile)
        re=list(reader2)
        print(tabulate(re,headers="keys",tablefmt="grid"))

main()
