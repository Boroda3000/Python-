class Vehicle:

    __color_variants = ['blue', 'red', 'yellow', 'green', 'purple', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        print(f'Марка и модель авто: {self.__model}')
    
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет авто: {self.__color}')
    
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец авто: {self.owner}')
        
    def set_color(self, new_color):
        for color in self.__color_variants:
            if new_color.upper() == color.upper():
                self.__color = new_color
                return
        print(f'Нельзя изменить цвет на {new_color}')
        return
        

class Sedan(Vehicle):

    __passengers_limit = 5




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()