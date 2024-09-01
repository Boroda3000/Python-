class House:
    houses_history = []

    def __new__(cls, *args):
        new_house = super().__new__(cls)
        cls.houses_history.append(args[0])
        return new_house


    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors


    def __len__(self):
        return self.num_of_floors


    def __str__(self):
        return f'Название дома: {self.name}, количество этажей: {self.num_of_floors}'
    

    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors
        elif isinstance(other, (int,float)):
            return self.num_of_floors == other
        else:
            print('Неверный тип данных')
    

    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors
        elif isinstance(other(int,float)):
            return self.num_of_floors < other
        else:
            print('Неверный тип данных')

    
    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors
        elif isinstance(other, (int,float)):
            return self.num_of_floors <= other
        else:
            print('Неверный тип данных')
    

    def __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors
        elif isinstance(other, (int,float)):
            return self.num_of_floors > other
        else:
            print('Неверный тип данных')
    

    def __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors
        elif isinstance(other, (int,float)):
            return self.num_of_floors >= other
        else:
            print('Неверный тип данных')


    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors
        elif isinstance(other, (int,float)):
            return self.num_of_floors != other
        else:
            print('Неверный тип данных')
    

    def __add__(self, other):
        if isinstance(other, House):
            return self.num_of_floors + other.num_of_floors
        if isinstance(other, (int, float)):
            return self.num_of_floors + other
        else:
            print('Невозможно сложить объект "House" с другим типом')


    def __radd__(self, other):
        return self.__add__(other)


    def __iadd__(self, other):
        if isinstance(other, House):
            self.num_of_floors += other.num_of_floors
            return self
        if isinstance(other, (int, float)):
            self.num_of_floors += other
            return self
        else:
            print('Невозможно сложить объект "House" с другим типом')


    def go_to(self, new_floor):
        if new_floor < 1  or new_floor > self.num_of_floors:
            print('Такого этажа не существует!')
        else:
            print(f'Выбранный этаж: {new_floor}')


    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Зеленая долина', 20)
print(House.houses_history)