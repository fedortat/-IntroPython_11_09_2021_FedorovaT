from argparse import ArgumentParser
import json
import csv
from random import uniform


class CurrencyConverter:
    def __init__(self):
        self.configs = "config.json"
        self.status = "status.csv"
        self.data = self.get_data_from_config()
        self.rate = self.get_rate()
        self.result = self.get_balance()
        self.balance = self.log_balance_to_csv()

    def get_data_from_config(self):  # считываем начальные данные из файла конфигурации
        with open(self.configs) as json_file:
            self.data = json.load(json_file)
        return self.data

    def get_rate(self, data):  # генерируем случайный курс
        self.rate = round(uniform((data["rate"] - data["delta"]), (data["rate"] + data["delta"])), 2)
        return self.rate

    def save_start_balance(self):  # сохраняем стартовый баланс в csv в первой строке
        start_balance = self.data
        start_balance = {key: start_balance[key] for key in
                         start_balance.keys() & {"rate", "usd_balance", "uah_balance"}}
        with open(self.status, "w", encoding="utf-8") as csv_file:  # сохраняем стартовый баланс в csv в первой строке
            fieldnames = ["rate", "usd_balance", "uah_balance"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(start_balance)

    def get_balance(self):  # получаем из файла с логом транзакций последнюю запись
        with open(self.status, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.result = [row for row in reader]
            self.result = dict(zip(self.result[0], self.result[-1]))
        return self.result

    def buy_usd(self, amount):  # функция для покупки USD и записи об этой транзакции в лог
        res = self.result
        usd_balance = float(res["usd_balance"])
        uah_balance = float(res["uah_balance"])
        result_b = 0
        curr_rate = self.rate(self.data)
        if amount * curr_rate <= uah_balance > 0:
            usd_balance += amount
            uah_balance -= amount * curr_rate
            result_b = {"rate": curr_rate, "usd_balance": usd_balance, "uah_balance": uah_balance}
            return self.balance(result_b)
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {amount * curr_rate}, AVAILABLE {uah_balance}")
        # return log_balance_to_csv(result_b)

    def sell_usd(self, amount):  # функция для продажи USD и записи об этой транзакции в лог
        res = self.result
        usd_balance = float(res["usd_balance"])
        uah_balance = float(res["uah_balance"])
        result_s = 0
        curr_rate = self.rate(self.data)
        if amount <= usd_balance > 0:
            usd_balance -= amount
            uah_balance += amount * curr_rate
            result_s = {"rate": curr_rate, "usd_balance": usd_balance, "uah_balance": uah_balance}
            return self.balance(result_s)
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {usd_balance}")
        # return log_balance_to_csv(result_s)

    def buy_all_usd(self):  # функция для покупки USD на все доступные гривны и записи об этой транзакции в лог
        res = self.result
        usd_balance = float(res["usd_balance"])
        uah_balance = float(res["uah_balance"])
        result_b = 0
        curr_rate = self.rate(self.data)
        if uah_balance > 0:
            usd_balance += uah_balance / curr_rate
            uah_balance = 0
            result_b = {"rate": curr_rate, "usd_balance": usd_balance, "uah_balance": uah_balance}
        return self.balance(result_b)

    def sell_all_usd(self):  # функция для продажи всех доступных USD и записи об этой транзакции в лог
        res = self.result
        usd_balance = float(res["usd_balance"])
        uah_balance = float(res["uah_balance"])
        result_s = 0
        curr_rate = self.rate(self.data)
        if usd_balance > 0:
            uah_balance += usd_balance * curr_rate
            usd_balance = 0
            result_s = {"rate": curr_rate, "usd_balance": usd_balance, "uah_balance": uah_balance}
        return self.balance(result_s)

    def log_balance_to_csv(self, new_balance, filename=self.status):  # сохраняем каждую транзакцию в csv
        with open(filename, "a", encoding="utf-8") as csv_f:
            fieldnames = ["rate", "usd_balance", "uah_balance"]
            wr = csv.DictWriter(csv_f, fieldnames=fieldnames)
            wr.writerow(new_balance)