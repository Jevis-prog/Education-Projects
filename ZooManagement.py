import Zoo
import Animals
import Zookeepers


zoo = Zoo.Zoo('My Zoo')
zoo.hire_zookeeper(Zookeepers.Zookeeper('Томас', 23))
zoo.add_animal(Animals.Bird('Кеша', 'Птица',3))

class ZooManagement:


    def __init__(self) -> None:
        print('\nЧем сегодня займемся в нашем зоопарке?: ')


    def start(self) -> None:
        while True:
            print('\n1. Добавить новое животное.')
            print('2. Показать список всех животных.')
            print('3. Нанять сотрудника.')
            print('4. Показать список всех сотрудников.')
            print('5. Посмотреть другие действия.')
            print('\n6. Закрыть смену.')
            action = input('\nВыберите действие: ')

            if action == '1': self.add_animal()
            elif action == '2': self.get_list_all_animals()
            elif action == '3': self.hire_an_employee()
            elif action == '4': self.show_list_all_employees()
            elif action == '5': self.show_another_actions()
            elif action == '6': break


    def add_animal(self) -> None:
        name = input('Введите имя: ')
        species = input('Введите вид: ')
        age = int(input('Введите возраст: '))
        if species.lower() == 'кошка':
            new_animal = Animals.Cat(name, species, age)
            zoo.add_animal(new_animal)
            print(f'\n{new_animal.name}, добро пожаловать в зоопарк!\n')
            print(new_animal.make_sound())
        elif species.lower() == 'птица':
            new_animal = Animals.Bird(name, species, age)
            zoo.add_animal(new_animal)
            print(f'\n{new_animal.name}, добро пожаловать в зоопарк!\n')
            print(new_animal.make_sound())
        elif species.lower() == 'собака':
            new_animal = Animals.Dog(name, species, age)
            zoo.add_animal(new_animal)
            print(f'\n{new_animal.name}, добро пожаловать в зоопарк!\n')
            print(new_animal.make_sound())


    def get_list_all_animals(self) -> None:
        print('\nВот список всех животных:')
        print(zoo.get_animals())


    def hire_an_employee(self) -> None:
        name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        new_zookeeper = Zookeepers.Zookeeper(name, age)
        zoo.hire_zookeeper(new_zookeeper)
        print(f'\n{new_zookeeper.name}, добро пожаловать в зоопарк!\n')


    def show_list_all_employees(self) -> None:
        print('\nВот список всех сотрудников:')
        print(zoo.get_zookeeper())


    def show_another_actions(self) -> None:
        while True:
            print('\n1. Назначить сотрудника следить за животным.')
            print('2. Покормить животное.')
            print('\n3. Назад.')

            action = input('\nВыберите действие: ')

            if action == '1': self.responsible_for()
            elif action == '2': self.feed_animl()
            elif action == '3': break


    def responsible_for(self) -> None:
        zookeeper_name = input('Введите имя сотрудника: ')
        animal_name = input('Введите имя животного: ')

        zookeeper = self.find_zookeeper(zookeeper_name)
        animal = self.find_animal(animal_name)

        if zookeeper and animal:
            zoo.assign_zookeeper_to_animal(zookeeper, animal)
            print(f'\n{zookeeper.name} теперь отвечает за {animal.name}.\n')
        else:
            print('\nСотрудник или животное не найдено.\n')

    def feed_animl(self) -> None:
        zookeeper_name = input('Введите имя сотрудника: ')
        animal_name = input('Введите имя животного: ')

        zookeeper = self.find_zookeeper(zookeeper_name)
        animal = self.find_animal(animal_name)

        if zookeeper and animal:
            print(zookeeper.feed_animal(animal))
        else:
            print('\nСотрудник или животное не найдено.\n')


    def find_zookeeper(self, name: str) -> Zookeepers.Zookeeper:
        for zk in zoo.zookeepers:
            if zk.name == name:
                return zk


    def find_animal(self, name: str) -> Animals.Animal:
        for an in zoo.animals:
            if an.name == name:
                return an


    def zzz(self):
        pass