import struct
import os


def OsOperation():
    os.remove("/home/kaviya-pt7969/sample.bin")


def FileOperation():
    with open("/home/kaviya-pt7969/sample.txt", "w+") as file:
        file.write("......The first content of saple.txt.....")
        file.seek(0)
        data = file.read()
        print(data)


def main():
    
    FileOperation()


main()
