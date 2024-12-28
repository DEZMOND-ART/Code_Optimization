import time
from multiprocessing import Pool

def read_info(name):    # Где name - название файла.
    # Функция должна:
    # Создавать локальный список all_data.
    all_data = []
    # Открывать файл name для чтения.
    with open(name, 'r') as f:
        # Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
        while True:
            line = f.readline()
            if not line:
                break
            # Во время считывания добавлять каждую строку в список all_data.
            all_data.append(line.strip())

if __name__ == '__main__':
    # Создайте список названий файлов в соответствии с названиями файлов архива.
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
# Вызовите функцию read_info для каждого файла, используя многопроцессорный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
# Для избежания некорректного вывода запускайте линейный вызов и многопроцессорный по отдельности, предварительно закомментировав другой.

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'{linear_time} (линейный)')
    # 6.738479137420654 (линейный)

    # Многопроцессорный
    start_time = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f'{multiprocess_time} (многопроцессорный)')
    # 2.778996467590332 (многопроцессорный)

