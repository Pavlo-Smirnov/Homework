#Task_1

import random

a = random.randint(1, 10)


def main():
    x = int(input('Your number: '))
    if x == a:
        print("You got it!")
    elif x > a:
        print("too high")
        main()  # why are you calling this recursively?
    else:
        print("too low")
        main()  # why are you calling this recursively?


main()



#Task_2

name = input("Your name: ")
age = int(input("Your age: "))
print('Hello %s, on your next birthday you’ll be %s years' % (name, age+1))

#Task_3

import random  # imports as you know now better place at the top of the file
word = input("Введіть слово: ")
y = 0
while y < 5:
    x = [i for i in word]
    random.shuffle(x)
    print(x)
    y += 1
