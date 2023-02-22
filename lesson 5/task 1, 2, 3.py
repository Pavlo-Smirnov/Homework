#Task_1

import random

a = random.randint(1, 10)


def main():
    x = int(input('Your number: '))
    if x == a:
        print("You got it!")
    elif x > a:
        print("too high")
        main()
    else:
        print("too low")
        main()


main()



#Task_2

name = input("Your name: ")
age = int(input("Your age: "))
print('Hello %s, on your next birthday you’ll be %s years' % (name, age+1))

#Task_3

import random
word = input("Введіть слово: ")
y = 0
while y < 5:
    x = [i for i in word]
    random.shuffle(x)
    print(x)
    y += 1
