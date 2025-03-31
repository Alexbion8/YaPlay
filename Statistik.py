import os

def col_poh_trekov():
    def count_lines_in_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    def get_track_word(count):
        if count % 10 == 1 and count % 100 != 11:
            return "трек"
        elif count % 10 in [2, 3, 4] and not (count % 100 in [12, 13, 14]):
            return "трека"
        else:
            return "треков"

    # Укажите путь к вашему файлу
    file_path = os.getcwd()+"/common_elements.txt"
    line_count = count_lines_in_file(file_path)

    if line_count is not None:
        track_word = get_track_word(line_count)
        #print(" ")
        return (f"У вас совпадает {line_count} {track_word}")



def proc_shoshesti():

    import os
    # Get the list of all files and directories
    path = os.getcwd()
    dir_list = os.listdir(path)
    dir_list.remove(".idea")
    dir_list.remove("venv")
    dir_list.remove("__pycache__")
    dir_list.remove("app.py")
    dir_list.remove("obs.py")
    dir_list.remove("templates")
    dir_list.remove("Statistik.py")
    dir_list.remove("common_elements.txt")
    dir_list.remove("icons8-телеграмма-app-64.png")

    def count_lines_in_file_prof_1(owner_file_path1):
        try:
            with open(owner_file_path1, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Файл {owner_file_path1} не найден.")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    def count_lines_in_file_prof_2(owner_file_path2):
        try:
            with open(owner_file_path2, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Файл {owner_file_path2} не найден.")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None

    # Укажите путь к вашему файлу
    owner_file_path1 = os.getcwd() + "/" + dir_list[0]
    line_count1 = count_lines_in_file_prof_1(owner_file_path1)
    owner_file_path2 = os.getcwd() + "/" + dir_list[1]
    line_count2 = count_lines_in_file_prof_2(owner_file_path2)

    if line_count1 is not None:
        max_chislo = [line_count1, line_count2]
        procent_1 = (min(max_chislo) / max(max_chislo)) * 100
        #print(" ")
        return (f"У вас соотношение {round(procent_1, 2)}% к 100%")



from collections import Counter

def analyze_file():
    # Словарь для хранения количества совпадений
    artist_counter = Counter()

    # Укажите путь к вашему TXT файлу
    file_path2 = os.getcwd() + "/common_elements.txt"

    # Чтение файла построчно
    with open(file_path2, 'r', encoding='utf-8') as file:
        for line in file:
            # Удаляем пробелы и символы новой строки
            line = line.strip()
            if line:  # Проверяем, что строка не пустая
                # Разделяем строку на ник и название
                try:
                    artist, title = line.split(' - ', 1)
                    artist_counter[artist] += 1  # Увеличиваем счетчик для исполнителя
                except ValueError:
                    print(f"Ошибка в строке: {line}. Не удалось разделить на ник и название.")

    # Получаем топ-3 исполнителей
    top_artists = artist_counter.most_common(3)

    # Выводим результаты
    print(" ")
    print("Топ-3 исполнителей:")
    for artist, count in top_artists:
        print(f"{artist} - {count} совпадений")

