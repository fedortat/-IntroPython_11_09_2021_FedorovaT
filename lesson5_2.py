# использование модулей (пакетов / библиотек)
import random  # импорт всего модуля

# from random import randint  # импорт конкретной функции из модуля

value = random.randint(1, 10)
print(value)

my_list = ["True", "False", "Unknown"]
my_choice = random.choice(my_list)  # случайный выбор из списка
print(my_choice)

random.shuffle(my_list)
print(my_list)

from string import ascii_lowercase as alphabet

print(alphabet, type(alphabet))
alphabet_list = list(alphabet)
random.shuffle(alphabet_list)
print(alphabet_list)


####################################################
# функции

def print_dict_custom(person):
    for key, value in person.items():
        # print(key, value)
        print(f"{key}: {value}")


my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
person = {"name": "John",
          "age": 23,
          "sex": "Male",
          "address": {"city": "Dnipro",
                      "street": "Polya",
                      "ZIP": "49000"
                      },
          "skills": {"hard": ["Python", "html", "DB", "C++"],
                     "soft": []
                     },
          }

# print(person)
# print_dict_custom(person)
print_dict_custom(my_dict)


def print_dict_custom(some_dict):
    for key, value in some_dict.items():
        # print(key, value)
        print(f"{key}: {value}")


my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
person = {"name": "John",
          "age": 23,
          "sex": "Male",
          "address": {"city": "Dnipro",
                      "street": "Polya",
                      "ZIP": "49000"
                      },
          "skills": {"hard": ["Python", "html", "DB", "C++"],
                     "soft": []
                     },
          }

# print(person)
print_dict_custom(person)
print_dict_custom(my_dict)
print_dict_custom(some_dict=my_dict)  # синхронизация названий


def print_dict_custom():  # так делать нельзя - всё, что используем, передаём в функцию!
    for key, value in person.items():
        # print(key, value)
        print(f"{key}: {value}")


my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58}
person = {"name": "John",
          "age": 23,
          "sex": "Male",
          "address": {"city": "Dnipro",
                      "street": "Polya",
                      "ZIP": "49000"
                      },
          "skills": {"hard": ["Python", "html", "DB", "C++"],
                     "soft": []
                     },
          }

# print(person)
print_dict_custom()


# генерация списка случайных чисел
def create_random_int_number_list(len_list=5): # через равно уствнавливается значение по умолчанию
    numbers = [random.randint(1, 10) for _ in range(len_list)]
    return numbers


result = create_random_int_number_list(5)
print(result)

# если нужно рандомной длины
len_list = random.randint(10, 20)
result = create_random_int_number_list(len_list)
print(result)


result = create_random_int_number_list() # если ничего не передаём, берётся значение по умолчанию
print(result)
