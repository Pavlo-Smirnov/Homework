a = 'pavel'
x = input("Write your name:")  # input("Write your name:").title() cause you always will get "Mistake" instead
if x == a or x == a.title():
    print("Welcome!")
else:
    print("Mistake")

