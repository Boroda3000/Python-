import time
import os
import multiprocessing

def read_info(name):
    all_data = []
    try:
        with open (name, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            for line in lines:
                all_data.append(line.strip())
            return all_data
    except FileNotFoundError:
        print(f"Файл '{name}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла '{name}': {e}")
        return []



base_path = r'D:\Python Project\module_10' 
filenames = [os.path.join(base_path, f'file {number}.txt') for number in range(1, 5)]

# start_time = time.time()
# result = list(map(read_info, filenames))
# end_time = time.time()
# execution_time = end_time - start_time
# print(f'Время выполнения: {execution_time} секунд(-ы).')

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.map(read_info, filenames)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Время выполнения: {execution_time} секунд')