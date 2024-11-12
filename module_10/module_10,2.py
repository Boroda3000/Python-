import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        counter = 0
        while enemies:
            print(f'{self.name} сражается {counter} дней, осталось победить {enemies} войнов!')
            enemies = enemies - self.power
            counter += 1
            time.sleep(2)
        print(f'{self.name} одержал победу спустя {counter} дня(дней)!')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()