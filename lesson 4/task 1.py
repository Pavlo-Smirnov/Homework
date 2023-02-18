x = 'helloworld'
if len(x) >= 2:
    print(x[0:2] + x[-2] + x[-1])
else:
    print("not valid")

x = "my"
if len(x) >= 2:
    print(x[0:2] + x[x.find('m')] + x[x.find('y')])
else:
    print("not valid")

y = 'x'
if len(y) == 2:
    print("it works")
elif len(y) <= 2:
    pass