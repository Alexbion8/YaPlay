import time

def OBSIE():
    # import OS module
    import os
    # Get the list of all files and directories
    path = os.getcwd()
    dir_list = os.listdir(path)
    dir_list.remove(".idea")
    dir_list.remove("venv")
    dir_list.remove("__pycache__")
    dir_list.remove("templates")
    dir_list.remove("app.py")
    dir_list.remove("obs.py")
    dir_list.remove("Statistik.py")
    dir_list.remove("icons8-телеграмма-app-64.png")

    # Функция для чтения данных из файла и возврата уникальных строк
    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)

    # Путь к вашим файлам
    file1_path = dir_list[0]
    file2_path = dir_list[1]
    output_file_path = 'common_elements.txt'

    # Чтение данных из файлов
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)

    # Нахождение общих элементов
    common_elements = data1.intersection(data2)

    # Сортировка общих элементов по алфавиту
    sorted_common_elements = sorted(common_elements)

    # Запись общих элементов в третий файл
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for element in sorted_common_elements:
            output_file.write(element + '\n')

