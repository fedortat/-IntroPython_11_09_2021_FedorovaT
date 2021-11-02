# 1)
my_number = 12305460003566300
############
# my_number = str(my_number)
# my_digit = "0"
# my_digit_count = my_number.count(my_digit)
# то же самое в одну строку:
zero_count = str(my_number).count("0")
print("1", zero_count)

# 2)
my_number = 12305460003566300
############
# my_number = str(my_number)
# count_zero_end = len(my_number) - len(my_number.rstrip('0'))
# print("2", count_zero_end)
# то же самое в одну строку:
count_zero_end = len(str(my_number)) - len(str(my_number).strip("0"))
print("2", count_zero_end)

# 3)
my_str = "96 больше чем 61 но меньше чем 316"
# my_digits_list = []
############
# my_str = my_str.split()
# for digit in my_str:
#     if digit.isdigit():
#         my_digits_list.append(int(digit))
# my_digits_sum = sum(my_digits_list)
############
# for word in my_str.split():
#     if word.isdigit():
#         my_digits_list.append(int(word))
# my_digits_sum = sum(my_digits_list)
# print("3", my_digits_sum)
# то же самое в одну строку:
my_digits_sum = sum([int(word) for word in my_str.split() if word.isdigit()])
print("3", my_digits_sum)

# 4)
my_str = "An example of a long random string"
l_limit = "e"
r_limit = "m"
############
# sub_str_start = my_str.find(l_limit)
# sub_str_end = my_str.rfind(r_limit)
# sub_str = my_str[sub_str_start + 1:sub_str_end]
# print(sub_str)
# то же самое в одну строку:
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print("4", sub_str)

# 5)
my_str_list = ["adghjk", "jfgagj", "aeitu", "fdgk", "oeapti", "lhljf"]
my_new_str_list = []
for word in my_str_list:
    if word[0] == "a":
        my_new_str_list.append(word)
# то же самое в одну строку:
my_new_str_list = [word for word in my_str_list if word[0] == "a"]

# 6)
my_str_list = ["adghjk", "jfgagj", "aeitu", "fdgk", "oeapti", "lhljf"]
my_new_str_list = []
for word in my_str_list:
    if "a" in word:
        my_new_str_list.append(word)
# то же самое в одну строку:
my_new_str_list = [word for word in my_str_list if "a" in word]

# 7)
my_list = [1, 2, 3, "11", "22", 33]
my_new_list = []
############
# for index in my_list:
#     if isinstance(index, str):
#         my_new_list.append(index)
############
# for index in my_list:
#     if type(index) == str:
#         my_list.append(index)
# то же самое в одну строку:
my_new_list = [index for index in my_list if isinstance(index, str)]

# 8)
my_str = "a string of random elements 12344"
# my_set = set(my_str)
# my_list = []
# for letter in set(my_set):
#     if my_str.count(letter) == 1:
#         my_list.append(letter)
# то же самое в одну строку:
my_list = [letter for letter in set(my_str) if my_str.count(letter) == 1]

# 9)
my_str_1 = "a string of random elements 12344"
my_str_2 = "another string of random elements 12234"
############
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
# same_symbols = my_str_1_set.intersection(my_str_2_set)
# same_symbols = list(same_symbols)
# то же самое в одну строку:
res_list = list(set(my_str_1).intersection(set(my_str_2)))
print("9", res_list)

# 10)
my_str_1 = "A string of random elements 123447"
my_str_2 = "another string of random elements 122345h"
my_list = []
for letter in my_str_1.lower():
    if my_str_1.lower().count(letter) == 1 and my_str_2.lower().count(letter) == 1:
        my_list.append(letter)

for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_list.append(symbol)
print("10", res_list)

# то же самое в одну строку:
my_list = [letter for letter in my_str_1.lower() if
           my_str_1.lower().count(letter) == 1 and my_str_2.lower().count(letter) == 1]

# 11)
my_str = "shdfjhjgk"
############
# my_list = []
# for index, item_alone in enumerate(my_str):
#     if index % 2 == 0:
#         result = my_str[index:index + 2]
#         if len(result) > 1:
#             my_list.append(result)
#         else:
#             my_list.append(item_alone + "_")
############
# if len(my_list) % 2:
#     my_str += "_"
# res_list = []
# for index in range(0, len(my_str), 2):
#     res_list.append(my_str[index:index + 2])
# print("11", res_list)

# то же самое в одну строку:
my_str = my_str + "_" if len(my_str) % 2 else my_str
res_list = [my_str[index:index + 2] for index in range(0, len(my_str), 2)]
print("11", res_list)
