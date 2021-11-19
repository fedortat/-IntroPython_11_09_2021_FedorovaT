from datetime import datetime

##################################################################
# 1)

class FilesWorker:
    def __init__(self, filename):
        self.filename = filename
        self.lines = self.read_file()

    def read_file(self):
        with open(self.filename, "r") as file:
            return file.read().split("\n")

    def get_domains(self):
        self.lines = [line.replace(".", "") for line in self.lines]
        return self.lines

    def get_names(self):
        self.lines = [line.split("\t")[1] for line in self.lines]
        return self.lines

    def get_dates(self):
        dates_dict = []
        for line in self.lines:
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


# для самопроверки

# filename = "domains.txt"
# files_worker = FilesWorker(filename)
# domains = files_worker.get_domains()
# print(domains)
#
# filename = 'names.txt'
# files_worker = FilesWorker(filename)
# names = files_worker.get_names()
# print(names)
#
# filename = 'authors.txt'
# files_worker = FilesWorker(filename)
# dates = files_worker.get_dates()
# print(dates)


##################################################################
# 2)

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.hp = 100
        self.strength = 1
        self.agility = 1
        self.intellect = 1

    def unit_heal(self):
        self.hp += 10
        self.hp = max(1, min(self.hp, 100))

    def unit_upgrade_strength(self):
        self.strength += 1
        self.strength = max(1, min(self.strength, 10))

    def unit_upgrade_agility(self):
        self.agility += 1
        self.agility = max(1, min(self.agility, 10))

    def unit_upgrade_intellect(self):
        self.intellect += 1
        self.intellect = max(1, min(self.intellect, 10))

    def __str__(self):
        return f"name: {self.name}, clan: {self.clan}, hp: {self.hp}, strength: {self.strength}, agility: {self.agility}, intellect: {self.intellect}"

    def __repr__(self):
        return f"{self.name} - {self.hp}"


# для самопроверки

# unit_1 = Unit("Wizard", "Wolves")
# unit_2 = Unit("Warrior", "Wolves")
#
# unit_1.unit_heal()
# unit_1.unit_upgrade_strength()
# unit_1.unit_upgrade_strength()
# unit_1.unit_upgrade_agility()
# unit_1.unit_upgrade_intellect()
#
# unit_2.unit_heal()
# unit_1.unit_upgrade_intellect()
# unit_1.unit_upgrade_intellect()
# unit_1.unit_upgrade_intellect()
# unit_1.unit_upgrade_intellect()
#
# print(unit_1)
# print(unit_2)
