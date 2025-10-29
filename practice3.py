from abc import ABC, abstractmethod


class Animal(ABC):
   
    kingdom = "Animalia"

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._protected_attr = "I am protected"    
        self.__private_attr = "I am private"        
    @abstractmethod
    def sound(self):
        pass

    def info(self):
        print(f"{self.name} is a {self.species} belonging to kingdom {Animal.kingdom}")

    @classmethod
    def describe_kingdom(cls):
        print(f"All animals belong to the kingdom {cls.kingdom}")

    @staticmethod
    def breathe():
        print("All animals need oxygen to breathe.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def sound(self):  
        print("Woof! Woof!")

    def info(self): 
        print(f"{self.name} is a {self.breed}, part of {self.species} species.")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def sound(self):
        print("Meow~")

def animal_sound(animal):
    animal.sound() 

dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "White")

dog1.info()
cat1.info()

Animal.describe_kingdom()
dog1.describe_kingdom()
Animal.breathe()
dog1.breathe()

print("\n--- Polymorphism Demo ---")
for animal in (dog1, cat1):
    animal_sound(animal)
print("\n--- Encapsulation Demo ---")
print(dog1._protected_attr) 
# print(dog1.__private_attr)  
print(dog1._Animal__private_attr)
