import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pat=r"\s?um[^a-zA-Z]"
    umlist=re.findall(pat,s,re.IGNORECASE)
    return len(umlist)

if __name__ == "__main__":
    main()
