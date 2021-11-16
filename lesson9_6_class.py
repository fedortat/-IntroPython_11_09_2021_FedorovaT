# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла в прописную (большую букву).
# Сделать щелчок Таноса - удалить половину случайных файлов из папки.

import os
from string import ascii_lowercase as alphabet
from random import shuffle


class AlphabetWorker:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.create_folder()

    def create_folder(self):
        os.makedirs(self.dir_name, exist_ok=True)

    def create_file(self, symbol):
        filename = f"{symbol}.txt"
        with open(f"{self.dir_name}/{filename}", "w") as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def create_alphabet_files(self):
        for symbol in alphabet:
            self.create_file(symbol)

    def do_thanos_click(self):
        # for filename in set(os.listdir(dir_name)):
        files = os.listdir(self.dir_name)
        shuffle(files)
        for filename in files[:len(files) // 2]:
            os.remove(os.path.join(dir_name, filename))


dir_name = "alphabet2"
alphabet_worker = AlphabetWorker(dir_name)
alphabet_worker.create_alphabet_files()
alphabet_worker.do_thanos_click()

# create_folder(dir_name)
# create_alphabet_files(dir_name)
# do_thanos_click(dir_name)
