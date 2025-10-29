import re

def isValid(ipid):
    if re.match(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$",ipid):
        return  True
    return False

def main():
    print(isValid(input("IP address: ").strip()))
main()