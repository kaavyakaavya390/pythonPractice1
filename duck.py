class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to quack!")

def make_it_quack(animal)->list[int]:
    animal.quack()
    return "hello"

make_it_quack(Duck())
make_it_quack(Person())