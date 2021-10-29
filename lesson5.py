# словари, методы словарей
# модули
# функции

my_dict = {"name": "John", "age": 23, 1: 11} # изменяемый, итерируемый тип данных. Порядок ключей не гарантируется!
print(my_dict, type(my_dict) == dict) # так можно определить тип данных

print(my_dict["name"]) # но если будет введен не существующий ключ, то прилетит ошибка
print(my_dict.get(111)) # get позволяет просто получить значение "ничего", а не ошибку, если будет введен не существующий ключ


person = {"name": "John", "age": 23}
# person["sex"] = "Male"
person.update({"sex": "Male"})
print(person)

person = {"name": "John", "age": 23}
person_details = {"sex": "Male", "address": "Dnipro"}
# person["sex"] = "Male"
person.update(person_details)
print(person)

#  если обновили справочник значениями из другого справочника, и какие-то данные ошибочные, то их можно принудительно перезаписать
person = {"name": "John", "age": 23}
person_details = {"sex": "Female", "address": "Dnipro"}
person.update(person_details)
print(person)
person["sex"] = "Male"
print(person)

# если совпадает ключ, то update перезаписывает предыдущее значение
person = {"name": "John", "age": 23}
person_details = {"sex": "Male", "address": "Dnipro", "name": "Jane"}
person.update(person_details)
print(person)

# если нужно не обновить текущий, а оставить старый и объединить его уже с другим
person = {"name": "John", "age": 23}
person_details = {"sex": "Male", "address": "Dnipro", "name": "Jane"}
# new_person = dict()
# new_person.update(person)
# new_person.update(person_details)
# то же самое, но в одну строку:
new_person = {**person, **person_details}
print(new_person)
# но тут важен порядок, если переставить, будет другое:
new_person = {**person_details, **person}
print(new_person)


my_tuple = (("name", "John"), ("age", 23))
person = dict(my_tuple)
print(person)

my_list = [["name", "John"], ["age", 23]]
person = dict(my_list)
print(person)


address = {"city": "Dnipro", "street": "Polya", "ZIP": "49000"}
person = {"name": "John", "age": 23}
person_details = {"sex": "Male", "address": address}
new_person = {**person_details, **person}
print(new_person["address"]["city"])


address = {"city": "Dnipro", "street": "Polya", "ZIP": "49000"}
skills = {"hard": ["Python", "html", "DB", "C++"], "soft": []}
person = {"name": "John", "age": 23, "skills": skills}
person_details = {"sex": "Male", "address": address}
new_person = {**person_details, **person}
new_person["skills"]["hard"].append("JS")
print(new_person)


# правильный вид записи:
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

# ключами могут быть только неизменяемые типы (строка, число, кортеж)

# my_dict = {1: 11, (1,2,3): "test", "1": "TEST"}
# print(11 in my_dict) # оператор in "смотрит" только в ключи
# print(my_dict.keys()) # метод keys создаёт объект и загоняет туда только ключи; dict_keys - это почти список ключей, но у него нет атрибутов списка,
# но его можно привести к типу списка:
# keys = list(my_list.keys())

# values = my_dict.values() # dict_values - это тоже почти список ключей, лучше приводить к типу списка
# print(values)
# for value in values:
#     print(value)
# items = my_dict.items()
# print(items)

my_dict = {"val_1": 12, "val_2": 24, "val_3": 6, "val_4": 58 }
# for key in my_dict: # цикл также идёт всегда по ключам
#     print(key, my_dict[key])
res_values = []
res_keys = []
for key, value in my_dict.items(): # items позволяет выводить пары, после чего можно работать и с ключом, и со значением
    if value > 10:
        res_values.append(value)
        res_keys.append(key)
print(res_values)
print(res_keys)


# в словаре могут быть одинаковые значения, но не могут быть ключи с одинаковым именем - тогда словарь перезапишет все только
# и возмёт только последнее значение
my_dict = {1: 11, 1: 22, 1: 33}
print(my_dict)

my_temp_dict = {11: 1, 12: 2, 13: 3}
print(my_temp_dict)
temp_reverse_dict = {value: key for key, value in my_temp_dict.items()}
print(temp_reverse_dict)

my_temp_dict = {11: 1, 12: 2, 13: 1}
if len(my_temp_dict.value()) == len(set(my_temp_dict.value)):
    temp_reverse_dict = {value: key for key, value in my_temp_dict.items()}
    print(temp_reverse_dict)