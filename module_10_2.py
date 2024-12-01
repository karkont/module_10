import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        total_enemies = 100
        day_count = 0
        print(f"{self.name}, на нас напали!")
        while total_enemies > 0:
            time.sleep(1)
            day_count += 1
            total_enemies = total_enemies - self.power
            print(f"{self.name} сражается {day_count} день(дня)..., осталось {total_enemies} воинов.")
            if total_enemies == 0:
                print(f"{self.name} одержал победу спустя {day_count} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")