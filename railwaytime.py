import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    pattern = r"^([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)\sto\s([1-9]|1[0-2])(:[0-5][0-9])?\s(AM|PM)$"

    match = re.fullmatch(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()
    start_min = start_min[1:] if start_min else "00"  
    end_min = end_min[1:] if end_min else "00"
    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_24 = to_24(start_hour, start_min, start_period)
    end_24 = to_24(end_hour, end_min, end_period)

    return f"{start_24} to {end_24}"


def to_24(hour, minutes, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    else: 
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minutes}"


if __name__ == "__main__":
    main()
