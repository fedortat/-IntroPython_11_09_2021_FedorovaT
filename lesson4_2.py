# ord, chr
# Генераторы списков (list comprehension)
# множества (set)

print(ord("a"))  # опреляет номер символа в таблице ASCII
print(chr(65))  # опреляет символ в таблице ASCII по номеру

########################################## Генераторы списков (list comprehension)
# alphabet_list = []
# for index_ascii in range(ord("a"), ord("z") + 1):
#     alphabet_list.append(chr(index_ascii))
# print(alphabet_list)
# alphabet = "".join(alphabet_list)
# print(alphabet)

# 2 способ:
alphabet_list = []
for index_ascii in range(ord("a"), ord("z") + 1):
    alphabet_list.append(chr(index_ascii))

alphabet_list = [chr(index_ascii) for index_ascii in range(ord("a"), ord("z") + 1)]
alphabet = "".join(alphabet_list)
print(alphabet)



result = [x ** 2 for x in range(10)]
print(result)



my_list = [12, -45, 23, 5, 0, 21, 900]
# res = []
# for value in my_list:
#     if value > 10:
#         res.append(value)
res = [value for value in my_list if value > 10] # and not value % 2]
print(res)


my_list = [12, -45, 23, 5, 0, 21, 900]
res = [str(value) * 20 for value in my_list if value > 10]
for line in res:
    print(line)

my_list = [12, -45, 23, 5, 0, 21, 900]
res = [str(value) * 20 for value in my_list if value > 10]
[print(line) for line in res]


########################################## Множества (set)
# Множества - изменяемый тип, только один представитель для каждого объекта, порядок не сохраняется

my_list = [1, 2, 3, 4, 5, 5, 5, "1"]
my_set = set(my_list)
print(my_set, type(my_set))


my_list = [1, 2, 3, 4, 5, 5, 5, "1"]
my_list_unique = list(set(my_list)) # deduplicate
my_set = set(my_list)
my_set.add(100)
print(my_set, type(my_set))

my_str_1 = "sgsgffsbgblsjfnsagjgkj"
my_str_2 = "vadhvsfvalgrjregiu4334r"
my_str_1_set = set(my_str_1)
my_str_2_set = set(my_str_2)

same_symbols = my_str_1_set.intersection(my_str_2_set)
print(same_symbols)

all_symbols = my_str_1_set.union(my_str_2_set)
print(all_symbols)

first_str_symbols = my_str_1_set.difference(my_str_2_set)
print(first_str_symbols)
second_str_symbols = my_str_2_set.difference(my_str_1_set)
print(second_str_symbols)