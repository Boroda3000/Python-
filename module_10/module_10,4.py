import threading
import random
import time
from queue import Queue

class Table:

    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        wait_time  = random.randint(3, 10)
        time.sleep(wait_time)
        print(f"{self.name} прием пищи закончил(-а).")

class Cafe:

    queue_guests = Queue()

    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            if isinstance(guest, Guest):
                Cafe.queue_guests.put(guest)
                print(f'{guest.name} ожидает в очереди.')
            else:
                print('Вы не в списке гостей, покиньте кафе, пожалуйста.')

    def discuss_guests(self):
        while not Cafe.queue_guests.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} прием пищи закончил(-а).")
                    print(f"Столик №{table.number} свободен.")
                    table.guest = None

            if not Cafe.queue_guests.empty():
                next_guest = Cafe.queue_guests.get() 
                available_table = next((t for t in self.tables if t.guest is None), None)
                if available_table: 
                    new_guest = Guest(next_guest.name) 
                    available_table.guest = new_guest
                    new_guest.start() 
                    print(f"{next_guest.name} сел(-а) за столик №{available_table.number}.")
            time.sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()