from random import randint, choice
from string import ascii_lowercase as alphabet


def create_email(names, domains):
    random_names = choice(names)
    random_domains = choice(domains)
    random_string = ''.join(choice(alphabet) for _ in range(randint(5, 7)))
    email = f"{random_names}.{randint(100, 999)}@{random_string}.{random_domains}"
    return email

def create_new_list(my_list):
    my_new_list = []
    for index, value in enumerate(my_list):
        if index % 2 != 0:
            my_new_list.append(value[::-1])
        else:
            my_new_list.append(value)
    return my_new_list

if __name__ == "__main__":  # если пишем такую строку, то дальнейший блок не включается при импорте из этого файла
    my_list = ["ddhfhsf", "esfhyh", "wrywty", "hlthklky"]  # для самопроверки
    my_new_list = create_new_list(my_list)
    print(my_new_list)

    names = ["john", "jane", "tom", "elis"]  # для самопроверки
    domains = ["net", "com", "ua"]
    email = create_email(names, domains)
    print(email)