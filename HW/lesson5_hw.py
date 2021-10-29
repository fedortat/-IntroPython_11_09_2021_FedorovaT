##################################################################
# 1)
persons = [{"name": "John", "age": 15}, {"name": "Jane", "age": 21}, {"name": "Jenny", "age": 21},
           {"name": "Tom", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Josephine", "age": 33}]
# а)
min_age_names = []
min_age = min(item["age"] for item in persons)
for item in persons:
    if item["age"] == min_age:
        min_age_names.append(item["name"])
print(min_age_names)

# б)
max_name_len = []
max_len = max(len(item["name"]) for item in persons)
for item in persons:
    if len(item["name"]) == max_len:
        max_name_len.append(item["name"])
print(max_name_len)

# в)
average_age = sum(item["age"] for item in persons) / len(persons)
# print(average_age)  # для самопроверки


##################################################################
# 2)
my_dict_1 = {"name": "John", "city": "Texas", "education": "TNU", "age": 15}
my_dict_2 = {"name": "Jack", "age": 45, "job": "engineer"}

# а)
common_keys = [key for key in my_dict_1 if key in my_dict_2]
# print(common_keys)  # для самопроверки

# б)
my_dict_1_keys = [key for key in my_dict_1 if key not in my_dict_2]
# print(my_dict_1_keys)  # для самопроверки

# в)
my_new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        my_new_dict[key] = value
# print(my_new_dict)  # для самопроверки

# г)
my_dict_united = {**my_dict_1, **my_dict_2}
for key, value in my_dict_united.items():
    if key in my_dict_1 and key in my_dict_2:
        my_dict_united[key] = [value, my_dict_1[key]]
# print(my_dict_united)  # для самопроверки

##################################################################
# 3)
def create_new_list(my_list):
    my_new_list = []
    for index, value in enumerate(my_list):
        if index % 2 != 0:
            my_new_list.append(value[::-1])
        else:
            my_new_list.append(value)
    return my_new_list

# my_list = ["ddhfhsf", "esfhyh", "wrywty", "hlthklky"]  # для самопроверки
# my_new_list = create_new_list(my_list)
# print(my_new_list)

##################################################################
# 4)
from random import randint, choice
from string import ascii_lowercase as alphabet


def create_email(names, domains):
    random_names = choice(names)
    random_domains = choice(domains)
    random_string = ''.join(choice(alphabet) for _ in range(randint(5, 7)))
    email = f"{random_names}.{randint(100, 999)}@{random_string}.{random_domains}"
    return email

# names=["john", "jane", "tom", "elis"]  # для самопроверки
# domains=["net", "com", "ua"]
# email = create_email(names, domains)
# print(email)