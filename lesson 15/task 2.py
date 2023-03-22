# 1) Create a class Dog with class attribute `age_factor` equals to 7.
# 2) Make __init__() which takes values for a dog’s age.
# 3) Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        print(my_dog.age * Dog.age_factor)


my_dog = Dog(int(input("What is your dog's age?: ")))
my_dog.human_age()







