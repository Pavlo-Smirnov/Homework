
def do_math():
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        result = a ** 2 / b
        print(result)

    except ZeroDivisionError:
        print("cannot be divided by zero")

    except ValueError:
            print("wrong input")

do_math()