class House:
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
            raise TypeError('Невозможно сложить объект "House" с другим типом')


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
            raise TypeError('Невозможно сложить объект "House" с другим типом')


    def go_to(self, new_floor):
        if new_floor < 1  or new_floor > self.num_of_floors:
            print('Такого этажа не существует!')
        else:
            print(f'Выбранный этаж: {new_floor}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Зеленая долина', 20)
h1.go_to(5)
h1.go_to(35)
h1.go_to(17)
h2.go_to(1)
h2.go_to(10)
h3.go_to(13)
h3.go_to(0)
print(len(h1))
print(len(h2))
print(len(h3))
x = h1 + h2
print(x)
h1 += h3
print(h1)