class Animal:

    def talk(self, word):
        self.word = word

    def choose_animal(self):
        x = input("Write your animal: ")
        if x == "dog" or x == "Dog":
            return a.talk("Woof")
        if x == "cat" or x == "Cat":
            return b.talk("Meow")

class Dog(Animal):
    def talk(self, word):
        print(f'Dog says: {word}')

class Cat(Animal):
    def talk(self, word):
        print(f'Cat says: {word}')

a = Dog()
b = Cat()

a.talk("Woof")
b.talk("Meow")

g = Animal()
g.choose_animal()







