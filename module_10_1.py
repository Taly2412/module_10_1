from threading import Thread
from datetime import datetime
import requests
from time import sleep


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1} \n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Время работы функции {time_res}')

time2_start = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourt = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourt.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourt.join()

time2_end = datetime.now()
time2_res = time2_end - time2_start
print(f'Время выполнения потока {time_res}')
