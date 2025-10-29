# class Dog:
#     num=500
#     def __init__(self, name):
#         self.name = name
#         self.num=504

#     def display_name(self):
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# # Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name}Guides the way!")

# # Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# # Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()
# print(lab.num)
# lab1=Labrador("Buddy1")
# lab1.num=600
# print(lab1.num)
# print(lab.num)


class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


class puppy(Dog):
    def __init__(self, puppy_name):
        self.puppy_name = puppy_name

    def change_breed(self, breed):
        self._breed = breed


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())
pup = puppy("kitty")
pup.name = "lucky"
print(pup.change_breed("golden"))
print(pup.name)
