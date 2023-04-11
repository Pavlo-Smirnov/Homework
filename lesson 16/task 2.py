class Mathematician:
    pass

    def square_numbers(self, list1):
        return [i ** 2 for i in list1]

    def remove_positives(self, list_with_numbers):
        return [i for i in list_with_numbers if i < 0]

    def filter_leaps(self, list_with_dates):
        return [i for i in list_with_dates if i % 4 == 0]


m = Mathematician()
assert m.square_numbers([2, 3, 4, 5]) == [4, 9, 16, 25]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
