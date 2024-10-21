from typing_extensions import Optional

import zoo
import animal
import zookeeper
from animal import Animal


class ZooManagement:


    def __init__(self) -> None:
        print('\nЧем сегодня займемся в нашем зоопарке?: ')
        self.zoo = zoo.Zoo('My Zoo')
        self.actions = {
            '1': ('Добавить новое животное.', self.add_animal),
            '2': ('Показать список всех животных.', self.show_list_all_animals),
            '3': ('Нанять сотрудника.', self.hire_an_employee),
            '4': ('Показать список всех сотрудников', self.show_list_all_employees),
            '5': ('Назначить сотрудника следить за животным.', self.responsible_for),
            '6': ('Покормить животное.', self.feed_animl)

        }
        self.page_size = 3

    def show_actions(self, page=1):
        actions_list = list(self.actions.items())
        total_pages = (len(actions_list) + self.page_size - 1) // self.page_size

        start = (page - 1) * self.page_size
        end = min(start + self.page_size, len(actions_list))

        print(f"\nДоступные действия (стр. {page}/{total_pages}):\n")

        for key, (description, _) in actions_list[start:end]:
            print(f'{key}. {description}')

        if page < total_pages:
            print('\ne. Следующая страница')
        if page > 1:
            print('\nq. Предыдущая страница')
        print('w. Завершить смену')

        return total_pages

    def select_action(self):
        page = 1
        while True:
            total_pages = self.show_actions(page)
            action = input('\nВыберите действие: ')

            if action == 'w':
                print('До завтра!')
                break
            elif action == 'q' and page > 1:
                page -= 1
            elif action == 'e' and page < total_pages:
                page += 1
            elif action in self.actions:
                _, action_func = self.actions[action]
                action_func()
            else:
                print('Неправильный выбор, попробуйте снова.')

    def add_animal(self) -> None:
        name = input('Введите имя: ')
        species = input('Введите вид: ')
        age = int(input('Введите возраст: '))

        new_animal: Animal

        if species.lower() == 'кошка':
            new_animal = animal.Cat(name, species, age)
        elif species.lower() == 'птица':
            new_animal = animal.Bird(name, species, age)
        elif species.lower() == 'собака':
            new_animal = animal.Dog(name, species, age)
        else:
            print('Неизвестный вид животного.')
            return

        self.zoo.add_animal(new_animal)  # Добавляем животное в зоопарк
        print(f'\n{new_animal.name}, добро пожаловать в зоопарк!\n')
        print(new_animal.make_sound())


    def show_list_all_animals(self) -> None:
        print('\nВот список всех животных:')
        print(self.zoo.get_animals())


    def hire_an_employee(self) -> None:
        name = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        new_zookeeper = zookeeper.Zookeeper(name, age)
        self.zoo.hire_zookeeper(new_zookeeper)
        print(f'\n{new_zookeeper.name}, добро пожаловать в зоопарк!\n')


    def show_list_all_employees(self) -> None:
        print('\nВот список всех сотрудников:')
        print(self.zoo.get_zookeeper())


    def responsible_for(self) -> None:
        zookeeper_name = input('Введите имя сотрудника: ')
        animal_name = input('Введите имя животного: ')

        zookeeper = self.find_zookeeper(zookeeper_name)
        animal = self.find_animal(animal_name)

        if zookeeper and animal:
            self.zoo.assign_zookeeper_to_animal(zookeeper, animal)
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


    def find_zookeeper(self, name: str) -> Optional[zookeeper.Zookeeper]:
        for zk in self.zoo.zookeepers:
            if zk.name == name:
                return zk
        return None


    def find_animal(self, name: str) -> Optional[zoo.Animal]:
        for an in self.zoo.animals:
            if an.name == name:
                return an
        return None



    def zzz(self):
        pass