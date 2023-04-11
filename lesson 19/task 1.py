
def with_index(iterable, start= 0):
    for i, item in enumerate(iterable, start= start):
        yield i, item

cars = ["BMW", "Volvo", "Opel", "Mazda", "Renaul"]
for i, car in with_index(cars):
    print(i)
