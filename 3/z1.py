class Zad1:
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def message(self):
        print(self.value1, self.value2)

m = Zad1(8, 19)
n = Zad1("Hello", "world!")

n.message()
m.message()    