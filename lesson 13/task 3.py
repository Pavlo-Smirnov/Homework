def shout():
    list1 = [-10, 12, -33, -64, 51]

    def add_num():
        b = [i ** 2 for i in list1 if i >= 0]
        return b

    print(add_num())

    def div_num():
        b = [i / 2 for i in list1 if i < 0]
        return b

    print(div_num())

shout()

