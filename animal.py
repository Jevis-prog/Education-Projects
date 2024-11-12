from abc import ABC, abstractmethod

class Animal(ABC):


    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        pass


    def info(self) -> str:
        return f'{self.name} - {self.species}, возраст: {self.age}'


    def __str__(self) -> str:
        return f'{self.name}'



class Cat(Animal):

    def make_sound(self) -> str:
        return f'{self.name} говорит: мууур'

class Dog(Animal):

    def make_sound(self) -> str:
        return f'{self.name} говорит: Гав'

class Bird(Animal):

    def make_sound(self) -> str:
        return f'{self.name} говорит: чирик'
