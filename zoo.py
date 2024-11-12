from animal import Animal
from zookeeper import Zookeeper


class Zoo:

    def __init__(self, zoo_name: str) -> None:
        self.zoo_name = zoo_name
        self.animals: list[Animal] = []
        self.zookeepers: list[Zookeeper] = []


    def get_animals(self) -> str:
        if not self.animals:
            return '\nВ зоопарке пока нет животных.\n'

        animal_info = [f'Имя: {animal.name}, Вид: {animal.species}, Возраст: {animal.age}' for animal in self.animals]
        return '\n'.join(animal_info)


    def get_zookeeper(self) -> str:
        if not self.zookeepers:
            return '\nВ зоопарке пока нет сотрудников.\n'

        zookeepers_info = [f'Имя: {zook.name}, Возраст: {zook.age}, Следит за: {zook.info()}' for zook in self.zookeepers]
        return '\n'.join(zookeepers_info)


    def add_animal(self, an: Animal) -> None:
        self.animals.append(an)


    def remove_animal(self, animal: Animal) -> None:
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print('Животное не найдено в зоопарке')


    def hire_zookeeper(self, zk: Zookeeper) -> None:
        self.zookeepers.append(zk)


    def assign_zookeeper_to_animal(self, zookeeper: Zookeeper, animal: Animal) -> None:
        print(f'{zookeeper.name} назначен следить за {animal.name}')
        zookeeper.lst_animal.append(animal)


    def list_animals_by_zookeeper(self, zookeeper: Zookeeper) -> str:
        return f'{zookeeper.name} следит за {[(animal) for animal in zookeeper.lst_animal]}'


    def animal_info(self, animal: Animal) -> str:
        return f'Информация о животном: {animal.name} - {animal.species}, возраст - {animal.age}'


