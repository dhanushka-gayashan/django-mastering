class Animal:

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('ANIMAL')

    def eat(self):
        print('EATING')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')

    def bark(self):
        print('WOOF')

    def eat(self):
        print('DOG EATING')


my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()