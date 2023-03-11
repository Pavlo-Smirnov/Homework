def some_math(x):
    def minus(y):
        return x - y

    return minus


minus_30 = some_math(30)


print(minus_30(10))
