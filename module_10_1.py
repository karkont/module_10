import time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}' + '\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time:.6f} секунд.")


t1 = threading.Thread(target=write_words,args=(10, 'example5.txt'))
t2 = threading.Thread(target=write_words,args=(30, 'example6.txt'))
t3 = threading.Thread(target=write_words,args=(200, 'example7.txt'))
t4 = threading.Thread(target=write_words,args=(100, 'example8.txt'))

start_thread_time = time.time()

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

end_thread_time = time.time()
print(f"Время выполнения потоков: {end_thread_time - start_thread_time:.6f} секунд.")