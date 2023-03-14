# 1) Make a class called Person.
# 2) Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# 3) Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson, and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def talk(self):
        print(f'Hello, it is {its_me.firstname} {its_me.lastname}. I am {its_me.age} years old.')


its_me = Person('Pavel', 'Smirnov', 25)
its_me.talk()

