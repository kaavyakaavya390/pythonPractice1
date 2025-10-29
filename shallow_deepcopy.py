from copy import copy

# *******for shallow copy*******
a = [[1, 2], 3]
b = copy(a)
b[0][1] = 10
print(a)
print(b)

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy(old_list)

old_list[0][0] = "AA"

print("Old list:", old_list)
print("New list:", new_list)
