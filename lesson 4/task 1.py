x = 'helloworld'
if len(x) >= 2:
    print(x[0:2] + x[-2] + x[-1])  # try negative indexes in slices
else:
    print("not valid")

x = "my"
if len(x) >= 2:
    print(x[0:2] + x[x.find('m')] + x[x.find('y')])  # try negative indexes in slices cause finding letter work only for this string
else:
    print("not valid")

y = 'x'
if len(y) == 2:
    print("it works")
elif len(y) <= 2:
    pass

