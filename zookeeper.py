from animal import Animal


class Zookeeper:


    def __init__(self, name: str, age: int, lst_animal=None) -> None:
        self.name = name
        self.age = age
        if lst_animal is None:
            lst_animal = []
        self.lst_animal = lst_animal


    def feed_animal(self, animal: Animal) -> str:
        print(animal.make_sound())
        return f'\n{animal.name} покормлен'


    def assign_animal(self, animal: Animal) -> None:
        self.lst_animal.append(animal)


    def info(self) -> str:
        animal_names = ', '.join(animal.name for animal in self.lst_animal)
        return f'{self.name} ухаживает за {[animal_names]}'


