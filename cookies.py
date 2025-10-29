class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.n = 0

    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if n < 0:
            raise ValueError("n should be non-negative")
        if self.n + n > self.capacity:
            raise ValueError("Exceeds capacity")
        self.n += n

    def withdraw(self, n):
        if self.n - n < 0:
            raise ValueError("Not enough cookies")
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n


def main():
    try:
        jar = Jar()
        jar.deposit(10)
        print(f"Capacity: {jar.capacity}")
        print(f"Size: {jar.size}")
        print(f"Cookies: {jar}")

        jar.withdraw(2)
        print(f"Capacity: {jar.capacity}")
        print(f"Size: {jar.size}")
        print(f"Cookies: {jar}")
        # jar.deposit(20)
    except ValueError as e:
        print("Error:", e)


main()
