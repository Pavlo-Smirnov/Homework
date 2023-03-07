# 1.Користувач вводить свій вік."
your_age = int(input("How old are you?"))
if your_age >= 18:
    print("You are adult")
else:
    print("You are underage")

# 2.Користувач вводить число. Якщо воно кратно 5 вивести "Діляться на 5". Якщо не кратно - "Не ділиться на 5"
x = int(input("Enter your number:"))
if x // 5:  # here you will get False expression only in case if result is zero, you need to check % operator for this
    print("Число делится на пять")
else:
    print("Число не делится на пять")

# 4.Користувач вводить оцінку.

mark = int(input("Enter your mark:"))
if mark == 1:
    print("Very bad")
elif mark == 2:
    print("Bad")
elif mark == 3:
    print("Not so bad")
elif mark == 4:
    print("Good")
elif mark == 5:
    print("Pretty Good")
else:
    print("Not Valid")

# 5.

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))
number_3 = int(input("Enter the third number:"))
pos_count, neg_count = 0, 0
if number_1 >= 0:
    pos_count += 1
if number_2 >= 0:
    pos_count += 1
if number_3 >= 0:
    pos_count += 1
if number_1 < 0:
    neg_count += 1
if number_2 < 0:
    neg_count += 1
if number_3 < 0:
    neg_count += 1

""" That seems more readable construction in my opinion"""
if number_1 >= 0:
    pos_count += 1
else:
    neg_count += 1
if number_2 >= 0:
    pos_count += 1
else:
    neg_count += 1
if number_3 >= 0:
    pos_count += 1
else:
    neg_count += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

# 6.Користувач вводить числа, які мають лежати в діапазоні від 10 до 100.
x = int(input("Enter your number between 10 and 100:"))
if 10 <= x <= 20:
    print("Your number is too small")
elif 20 <= x <= 50:
    print("Your number is average")
elif 50 <= x <= 100:
    print("Your number is big")
else:
    print("Your number is not valid")
