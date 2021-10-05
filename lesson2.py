# if условие_1:
#     блок, если да (условие_1)
# elif условие_2:
#     блок, если да (условие_2)
# else:
#     блок, если нет


case = 6
if case == 6:
    print("Победил Вася!")
elif case == 1:
    print("Победил Петя!")
else:
    print("Все проиграли!")


case = input("Кинь кубик:")  # всегда str
# case = int(case)
print(case)
if case == "6":
    print("Победил Вася!")
elif case == "1":
    print("Победил Петя!")
else:
    print("Все проиграли!")


from random import randint

case = randint(1, 6)
print("Выпало число", case)
if case == 6:
    print("Победил Вася!")
elif case == 1:
    print("Победил Петя!")
else:
    print("Все проиграли!")

########################################
# тернарный оператор - однострочная форма записи такого блока:
if case > 3:
    result = case ** 2
else:
    result = - case

result = case ** 2 if case > 3 else - case

print("Выпало число", case, "Результат:", result)

########################################
# СТРОКИ и методы строк
# форматирование строк

case = 1
result = 2
print(f"Выпало число:{case} c результатом:{result}")

dirname = "home"
filename = "test.py"
path = f"{dirname}/{filename}"
print(path)

# литералы строк
my_str_1 = "I'm Qwerty"
my_str_2 = '"Apple" Inc.'
my_str_3 = '''Zxcvbn'''
my_str_4 = """I'm "Apple" Inc."""

index = 2  # индекс - 1 это последний с конца строки
symbol = my_str_1[index]
print(symbol)

my_str_1_len = len(my_str_1)
print(my_str_1_len, my_str_1[my_str_1_len - 1])

# срез строки
my_str_1 = "I'm Qwerty"
new_str = my_str_1[1:5] # часть строки от левого индекса (включительно) до правого индекса (не включительно)

print(new_str)

my_str_1 = "I'm Qwerty"
index = 5
new_str = my_str_1[: index] + "K" + my_str_1[index + 1:] # замена символа на конкретном месте в строке
print(new_str)

# new_str = my_str_1[1:-1:3] # 3 - шаг среза
# new_str = my_str_1[::2] # символы на чётных местах
# new_str = my_str_1[1::2] # символы на нечётных местах
new_str = my_str_1[::-1] # разворот строки
print(new_str)

my_str_1 = "IIIIeeeee'm Qwerty"

if my_str_1[-1] == "a":
    print(f"'a' on last position {my_str_1}")
else:
    print(f"'a' not on last position {my_str_1}")

for symbol in my_str_1: # строка - итерируемый объект
    if (symbol.lower() not in "eyuioa") and symbol.isalpha() and symbol.isupper():
        print(symbol)

for symbol in my_str_1:
    print(f"symbol '{symbol}' --> {ord(symbol)}")

for index in range(32, ord('z') + 1, 2):
    print(f"index: {index} --> '{chr(index)}'")

count = 0
do_loop = True

while count < 10:
    print("This is while loop", count)
    count += 1


# while True:
#     print("This is while loop", count)
#     count += 1
#     if count > 10
#         break