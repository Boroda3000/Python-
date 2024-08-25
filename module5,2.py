class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors


    def __len__(self):
        return self.num_of_floors


    def __str__(self):
        return f'Название дома: {self.name}, количество этажей: {self.num_of_floors}'


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
print(h1)
print(h2)
print(h3)