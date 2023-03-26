class Fraction:
    pass

    def __init__(self, number):
        self.number = number
        if not isinstance(number, int):
            raise TypeError("The object must be integer")

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        return self.number + int(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        return self.number - int(other)

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        return self.number / int(other)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        return self.number * int(other)

    def __gt__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        if self.number > other:
            print(f"True, {self.number} is greater than {other}")
        else:
            print(f"False, {other} is greater than {self.number}")

    def __lt__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        if self.number < other:
            print(f"True, {self.number} is less than {other}")
        else:
            print(f"False, {other} is less than {self.number}")

    def __eq__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        if self.number == other:
            print(f"True, {self.number} is equal to {other}")
        else:
            print(f"False, {self.number} is not equal to {other}")

    def __ne__(self, other):
        if not isinstance(other, int):
            raise TypeError("You can use only integers")
        if self.number != other:
            print(f"True, {self.number} is not equal to {other}")
        else:
            print(f"False, {self.number} is equal to {other}")




f1 = Fraction(50)
print(f1 + 12)
print(f1 - 12)
print(f1 / 12)
print(f1 * 12)
f1.__gt__(49)
f1.__lt__(49)
f1.__eq__(50)
f1.__ne__(75)




