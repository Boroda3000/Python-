import threading
import random
import time

lock = threading.Lock()

class Bank:

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self):
        global lock
        i = 0
        while i <= 100:
            random_num = random.randint(50, 500)
            self.balance += random_num
            print(f'Пополнение:{random_num}. Текущий баланс:{self.balance}.')
            time.sleep(0.001)
            i += 1
            if self.balance > 500 and lock.locked() is True:
                lock.release()

    def take(self):
        global lock
        j = 0
        while j <= 100:
            random_num = random.randint(50, 500)
            print(f'Запрос на снятие {random_num}.')
            j += 1
            if random_num > self.balance:
                print('Запрос отклонен, недостаточно средств.')
                lock.acquire()
            else:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Текущий баланс:{self.balance}.')


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
