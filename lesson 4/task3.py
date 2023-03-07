a = float(input("Mathematical expression: 10 * 10 ="))  # float is a good point
if a == 100:
    print("Good!")
else:
    print("Try one more time")


# Just more universal variant
a, b = int(input("First value: ")), int(input("Second value: "))
if float(input(f"Mathematical expression: {a} * {b} =")) == a * b:
    print("Good!")
else:
    print("Try one more time")
