from collections import deque

fruits = ["apple", "orange", "banana", "pineapple", "guava"]
fruits.sort()
print("fruits.sort()", fruits)
fruits.append(1)
print("fruits.append(1)", fruits)
fruits.reverse()
print("fruits.reverse()", fruits)
fruits.pop()
print("fruits.pop()", fruits)

# ------deque------
queue = deque()
queue.appendleft(fruits[0])
print("queue.appendleft(fruits[0])", queue)
queue.appendleft(fruits[2])
print("queue.appendleft(fruits[2])", queue)
queue.pop()
print("queue.pop()", queue)

# -----listcomprehension-------
squares = [x**2 for x in range(10)]
print(squares)
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# -------dictionary......
dictionary = dict()
dictionary["Apple"] = 50
dictionary["Orange"] = 30
dictionary["Graps"] = 35
print(dictionary.__dict__())
for k, v in dictionary.items():
    print(f"{k} : {v}")
print(dictionary["Orange"])
print(dictionary.keys())
print(dictionary.values())

# ------------tuples-----------
tup = ([120, 30, "apple", 89, 34, 45], 55, 24)
tup2 = 30, 39, 38, 37, 36
tup3 = tup + tup2
print(tup3)
print(tup[0])
print(tup[1])
print(tup[0][3])
tup[0][3] = "orange"
print(tup[0][3])
print(tup)
