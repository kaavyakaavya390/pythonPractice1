# === FILE===


with open("example.txt", "w") as f:
    f.write("Line 1: Hello Python!\n")
    f.write("Line 2: File handling demo\n")

with open("example.txt", "a") as f:
    f.write("Line 3: Appending new text\n")

lines_to_write = [
    "Line 4: Written using writelines()\n",
    "Line 5: Another line\n"
]
with open("example.txt", "a") as f:
    f.writelines(lines_to_write)

with open("example.txt", "r") as f:
    data = f.read()
    print("-------------------------------------")
    print(data)

with open("example.txt", "r") as f:
    print("-------------------------------------")
    print(f.readline().strip())  
    print(f.readline().strip())


with open("example.txt", "r") as f:
    all_lines = f.readlines()
    print("-------------------------------------")
    print(all_lines)

with open("example.txt", "r") as f:
    print("-------------------------------------")
    print("Current position:", f.tell())  
    f.read(10)
    print("After reading 10 chars, position:", f.tell())
    f.seek(0)
    print("After seek(0), position:", f.tell())
    print("First 5 chars after seek:", f.read(5))
