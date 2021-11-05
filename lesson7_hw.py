import json
import re

##################################################################
# 1)
def read_json_file(filename):
    with open(filename, "r") as json_file:
        json_data = json.load(json_file)
    return json_data

filename = "data.json"
json_data = read_json_file(filename)
# print(json_data)


##################################################################
# 2)
def sort_by_last_name(json_data):
    last_name = json_data["name"].split(" ")[-1]
    return last_name

# для самопроверки
# sorted_data_by_name = sorted(json_data, key=sort_by_last_name)
# print(sorted_data_by_name)


##################################################################
# 3)
def sort_by_death_date(json_data):
    death_date = re.findall(r"[0-9]+", json_data["years"])[-1]
    death_date = -int(death_date) if "BC" in json_data["years"] else int(death_date)
    return death_date

# для самопроверки
# sorted_data_by_death_date = sorted(json_data, key=sort_by_death_date)
# print(sorted_data_by_death_date)


##################################################################
# 4)
def sort_by_text_len(json_data):
    text_len = len(json_data["text"].split(" "))
    return text_len

# для самопроверки
# sorted_data_by_text_len = sorted(json_data, key=sort_by_text_len)
# print(sorted_data_by_text_len)