class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.iterable):
            result = self.iterable[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.iterable[index]

my_iterable = MyIterable([1, 2, 3, 4, 5])
for element in my_iterable:
    print(element)
print("Retrieve an element", my_iterable[3])