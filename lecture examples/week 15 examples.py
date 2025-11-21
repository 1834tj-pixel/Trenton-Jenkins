class Animal:
    def __int__(selfz name: str):
    self.name = name
    self.alive = True

    def __str__(self):
        return f'Animal {self.name} is alive?: {self.alive}'

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')

class Dog(Animal):
    def __init__(selfself, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def__str__(self):
    return f'{self.name} is {self.breed}.'

    def bark(self):
        print(f'{self.name} is barking. Woof!}')
def main() -> None:
    generic_ animal + Animal('Leo')
    generic_animal.eat()
    generic_animal.sleep()

    print('-' * 20)

    my_dog = Dog(name"Buddy', breed:"Golden Retriever')
    my_dog.eat()
    my_dog.sleep()
    my_dog.bark()

    my_animals: list = []