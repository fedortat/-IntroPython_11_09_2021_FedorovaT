##################################################################
# 1)
def create_domains_list(filename):
    with open(filename, "r") as txt_file:
        return [line.strip()[1:] for line in txt_file.readlines()]
    return domains_list

# filename = "domains.txt"  # для самопроверки
# domains_list = create_domains_list(filename)
# print(domains_list)



##################################################################
# 2)
def create_names_list(filename):
    with open(filename, "r") as txt_file:
        return [line.split("\t")[1] for line in txt_file.readlines()]
    return names_list

# filename = "names.txt"  # для самопроверки
# names_list = create_names_list(filename)
# print(names_list)


##################################################################
# 3)
from datetime import datetime

def create_dates_dict(filename):
    dates_dict = []
    with open(filename, "r") as txt_file:
        for line in txt_file.readlines():
            my_str = line.split(" - ")
            if len(my_str) > 1:
                date = my_str[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                dates_dict.append(
                    {"date_original": date,
                    "date_modified": datetime.strftime(my_date, "%d/%m/%Y")}
                )
    return dates_dict

# filename = "authors.txt"  # для самопроверки
# dates_dict = create_dates_dict(filename)
# print(dates_dict)

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split("\n")

def get_domains(filename):
    lines = read_file(filename)
    lines = [line.replace(".", "") for line in lines]
    return lines

def get_names(filename):
    lines = read_file(filename)
    lines = [line.split("\t")[1] for line in lines]
    return lines

def str_to_date(some_str):
    months_dict = {"January": "01",
                 "February": "02",
                 "March": "03",
                 "April": "04",
                 "May": "05",
                 "June": "06",
                 "July": "07",
                 "August": "08",
                 "September": "09",
                 "October": "10",
                 "November": "11",
                 "December": "12"}
    parts = some_str.split()
    day, month, year = parts
    date = f"{day[:-2].zfill(2)}/{months_dict[month]}/{year}"
    return date

def get_dates(filename):
    lines = read_file(filename)
    lines = [line.split(" - ")[0] for line in lines if " - " in line]
    lines = [str_to_date(line) for line in lines]
    return lines


filename_domains = 'domains.txt'
domains = get_domains(filename_domains)
print(domains)

filename_names = 'names.txt'
names = get_names(filename_names)
print(names)

filename_dates = 'authors.txt'
dates = get_dates(filename_dates)
print(dates)