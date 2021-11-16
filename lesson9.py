# ООП
#########################

from lesson9_class import DataUser

########################### начало ООП
# class DataUser: # весь класс
#     # просто атрибуты класса - плохая практика
#     name = "" # атрибут класса
#     ip = "0.0.0.0" # атрибут класса
#     user_time = 0.0 # атрибут класса

# data_user_1 = DataUser()  # экземпляр класса
# data_user_2 = DataUser()  # экземпляр класса
# data_user_3 = DataUser()  # экземпляр класса
#
# # что нужно, чтобы поменять данные
# DataUser.ip = "127.0.0.1"  # меняем для всего класса
# data_user_1.ip = "127.0.0.2"  # меняем для экзмепляра класса
# data_user_2.ip = "255.255.255.0"
# data_user_1.error_count = 3  # добавляем новый атрибут для экземпляра класса
#
# print(data_user_1.ip)
# print(data_user_2.ip)
# print(data_user_1, data_user_2, data_user_3)
# print(data_user_1.error_count)
# print(DataUser.ip)

########################### атрибут экзмепляра класса

data_user_1 = DataUser("John", "127.0.0.2", 10.0)
data_user_2 = DataUser("Jack", "255.255.255.0", 0.0)
# print(data_user_1.ip)
# print(data_user_2) # напечатает значения, если мы создадим для этого вывод через __str__(self),
# иначе просто обозначит объект в памяти
print(data_user_1)
# users = [data_user_1, data_user_2] # так не распечатает, нужно создать вывод через __repr__(self)
# print(users)
add_time = 2.0  # добавляем 2 минуты через наш кастомный метод для класса - increase_user_time
data_user_1.increase_user_time(add_time)

# плохая практика:
# user_time = data_user_1.user_time
# user_time += add_time
# data_user_1.user_time = user_time

print(data_user_1)
