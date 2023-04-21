class Jar:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.capacity
        ...

    # adds cookies to the jar, if adding it exceeds capacity raise
    # ValueError instead.
    def deposit(self, n):
        self.capacity = self.capacity + n

    def withdraw(self, n):
        if (self.capacity == 0):
            raise ValueError
        self.capacity = self.capacity - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or capacity > 12:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._capacity


def main():
    cookie = Jar(3)
    extra_cookie = cookie.deposit(1)
    removed_cookie = cookie.withdraw(3)
    # print(cookie)
    # print(cookie.size)
    print(str(Jar()))


if __name__ == "__main__":
    main()
