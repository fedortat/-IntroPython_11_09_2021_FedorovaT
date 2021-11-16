############ lambda
my_list = [1, -4, 0.5, 100]

sort_list = sorted(my_list, key=abs)
print(sort_list)

# если хотим посортировать по близости к числу 50, можно через короткую запись функции
# lambda - это функция в одну строку, без названия, на лету
sort_list = sorted(my_list, key=lambda x: abs(50 - x))
print(sort_list)

persons = [{"name": "John", "age": 15},
           {"name": "Jane", "age": 21},
           {"name": "Jenny", "age": 21},
           {"name": "Tom", "age": 33},
           {"name": "Jack", "age": 45},
           {"name": "Josephine", "age": 33}]

sort_by_age = sorted(persons, key=lambda x: (x["age"], len(x["name"])))
print(sort_by_age)

# если мы хоти сделать пары из двух списков, можно использовать функцию zip
first = [1, 2, 3, 4, 5]
second = [9, 8, 7, 6, 5]
# но нужно привести результат к какому-то типу:
# result = list(zip(first, second))
result = dict(zip(first, second))
print(result)

# если у какого-то набор короче, чем у другого, то ошибки не будет,
# просто закончится парование на элементе самого короткого

# можно также добавлять и строки:
first = [1, 2, 3, 4, 5]
second = [9, 8, 7, 6, 5]
test = list("qwerty")

result = list(zip(first, second, test))
print(result)
# но для словарей такой вариант не сработает - он не поймёт, что делать с лишним символом

first = [1, 2, 3, 4, 5]
result = [str(numb) for numb in first]
# функция map применяет какую-то одну функцию к какому-то набору,
# для неё также нужно делать приведение к типу
result = list(map(str, first))
print(result)

first = [1, 2, 3, 4, 5]
result = [numb ** 2 for numb in first]
print(result)

result_map = list(map(lambda x: x ** 2, first))
print(result_map)
