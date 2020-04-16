class Dog:

    # Class Attributes
    species = "mammal"

    def __init__(self, breed, name):
        # Object Attributes
        self.breed = breed
        self.name = name


myDog = Dog("Lab", "Sammy")

print(myDog.breed)
print(myDog.name)

print(Dog.species)
