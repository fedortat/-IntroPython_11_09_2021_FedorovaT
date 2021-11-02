##################################################################
# 1)
def create_domains_list(filename):
    with open(filename, "r") as txt_file:
        return [line.strip()[1:] for line in txt_file.readlines()]
    return damians_list

# filename = "domains.txt"  # для самопроверки
# damians_list = create_domains_list(filename)
# print(damians_list)


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