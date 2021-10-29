############################################### параметры функции

# генерируем случайный треугольник
# triangle_abc = {"A": (2, 3),
#                 "B": (-4, 7),
#                 "C": (0, 0)}

from random import randint

MIN_LIMIT = 1  # большими буквами можно обозначить глобальные параметры, которые будут применяться дальше где угодно по коду
MAX_LIMIT = 10


def create_point(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    return (randint(min_limit, max_limit), randint(min_limit, max_limit))


# def create_triangle(min_limit, max_limit):
#     # triangle_dict = {"A": (randint(1, 10), randint(1, 10)), # DRY (don't repeat yourself)
#     #                  "B": (randint(1, 10), randint(1, 10)),
#     #                  "C": (randint(1, 10), randint(1, 10))}
#     triangle_dict = {"A": create_point(min_limit, max_limit),
#                      "B": create_point(min_limit, max_limit),
#                      "C": create_point(min_limit, max_limit)}  # можно указать конкретные значение под конкретную точку
#     return triangle_dict

# triangle_abc = create_triangle(min_limit=-10, max_limit=10)
# print(triangle_abc)

def create_triangle(name="ABC"):
    # triangle_dict = {"A": (randint(1, 10), randint(1, 10)), # DRY (don't repeat yourself)
    #                  "B": (randint(1, 10), randint(1, 10)),
    #                  "C": (randint(1, 10), randint(1, 10))}
    triangle_dict = {name[0]: create_point(),
                     name[1]: create_point(),
                     name[2]: create_point()}  # можно указать конкретные значение под конкретную точку
    return triangle_dict


def create_triangles_list(number=3):
    return [create_triangle("QWE") for _ in range(number)]


triangles_list = create_triangles_list()
print(triangles_list)


############################################### именованые параметры функции
# def test_func(par_1: str, par_2: str, par_3, par_4: str = "asdfgh") -> int:  # стрелочкой указывается ожидамый тип на выходе
#     return f"{len(par_1)}_{len(par_2)}_{par_3}_{len(par_4)}"

# def test_func_2(*args):
#     return "__".join(args)
#
# print(test_func_2("qw", "er", "1111", "svgbgb"))

def test_func_2(*args, **kwargs):
    print(args)
    print(kwargs)


print(test_func_2("John", 24, job="programmer", animal="dog"))

############################################### модуль os
import os

# dir = os.listdir()
# print(dir)

dir = os.listdir("HW")
print(dir)

filename = "lesson4_hw.py"
folder = "HW"
# path = f"{folder}/{filename}"
# path = os.path.join(folder, filename)
# path = os.path.join(os.getcwd(), folder, filename)
# print(path)
# os.makedirs("test1/test2", exist_ok=True)

for filename in sorted(dir):
    file_path = os.path.join("HW", filename)
    if os.path.isfile(filename):
        print(f"{filename=}")

############################################### работа с файлами
# менеджер контекста:
# with open("HW/lesson4_hw.py", "r") as file:
#     data = file.read()  #считал всё одной строкой
# print(data)

# старый способ - лучше не использовать:
# file = open("HW/lesson4_hw.py", "r")
# data = file.read()
# file.close()
# print(data)


# with open("HW/lesson4_hw.py", "r") as file:
#     data = file.readlines()
# print(data)
#
# data.append("Test\n")
#
# with open("HW/lesson4_test_hw.py", "w") as file:
#     file.writelines(data)


############################################### practice
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла в прописную (большую букву).
# Сделать щелчок Таноса - удалить половину случайных файлов из папки.

import os
from string import ascii_lowercase as alphabet
from random import shuffle


def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def create_file(symbol, folder_name):
    filename = f"{symbol}.txt"
    with open(f"{folder_name}/{filename}", "w") as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))


def create_alphabet_files(folder_name):
    for symbol in alphabet:
        create_file(symbol, folder_name)


def do_thanos_click(dir_name):
    # for filename in set(os.listdir(dir_name)):
    files = os.listdir(dir_name)
    shuffle(files)
    for filename in files[:len(files) // 2]:
        os.remove(os.path.join(dir_name, filename))

dir_name = "alphabet"
create_folder(dir_name)
create_alphabet_files(dir_name)
do_thanos_click(dir_name)
