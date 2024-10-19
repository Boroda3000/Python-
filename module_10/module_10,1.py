from threading import Thread
from time import sleep

def write_words(word_count, file_name):

    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            word = f"Море волнуется {i}"
            file.write(word + '\n')
            print(f"Записано: {word}")
            sleep(0.1)
    print(f"Запись в файл {file_name} завершена.")


# write_words(10, 'example1.txt')
# write_words(30, 'example2.txt')
# write_words(200, 'example3.txt')
# write_words(100, 'example4.txt')

thr_1 = Thread(target = write_words, args = (10, 'example1.txt'))
thr_2 = Thread(target = write_words, args = (30, 'example2.txt',))
thr_3 = Thread(target = write_words, args = (200, 'example3.txt',))
thr_4 = Thread(target = write_words, args = (100, 'example4.txt',))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()