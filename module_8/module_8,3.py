class Car:

    def __init__(self, model, __vin, __number):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__number):
            self.__number = __number

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin-номера.')
        if 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin-номера.')
        else:
            return True
        
    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров.')
        if len(number) != 6:
            raise IncorrectCarNumber('Неверная длина номера.')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')