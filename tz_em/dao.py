# Файл dao.py - Data Access Object (Объект доступа к данным)

import csv
from pprint import pprint


NAME_FILE = 'telephone_directory.csv'


# Чтение из CSV файла
def file_read() -> list:
    with open(NAME_FILE, 'rt') as fin:
        cin = csv.reader(fin)
        result = [row for row in cin]
        return result


# Запись в CSV файл
def file_write(data: list) -> None: # заменить list на list[схема]
    with open(NAME_FILE, 'wt') as fout:
        csvout = csv.writer(fout)
        csvout.writerows(data)







if __name__ == "__main__":  
    #           Фамилия      Имя      Отчество      Компания                       Рабочий тел.       Личный тел.
    test_data = [['Комаров', 'Денис', 'Валерьевич', 'ФАУГ НИИ Авиационных Систем', '+7 922 836 5869', '+7 922 842 6019'],
                ['Михайлов', 'Игорь', 'Дмитриевич', 'ФСИ', '+7 922 839 0890', '+7 922 842 6222'],
                ['Сосунов', 'Иван', 'Иванович', 'Effective Mobile', '+7 922 843 5581', '+7 922 843 0777'],
                ['Пупкин', 'Василий', 'Васильевич', 'ТКС', '+7 922 843 2431', '+7 922 843 5807']]
    
    # file_write(test_data)
    # file_read()




