import threading
import time
from random import random, randint



class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            deposit_change = randint(50, 500)
            self.balance += deposit_change
            print(f"Пополнение: {deposit_change}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            deposit_change = randint(50, 500)
            print(f"Запрос на {deposit_change}")
            if deposit_change <= self.balance:
                self.balance -= deposit_change
                print(f"Снятие: {deposit_change}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))


th1.start()
th2.start()


th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')