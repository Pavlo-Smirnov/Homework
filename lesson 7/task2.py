prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0
for x in prices:
    total = total + prices[x] * stock[x]  # total += prices[x] * stock[x]

    print(total)