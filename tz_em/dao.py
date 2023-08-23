# Файл dao.py - Data Access Object (Объект доступа к данным)

import csv
from pandas import read_csv, DataFrame


COLUMNS = ['Фамилия', 'Имя', 'Отчество', 'Компания', 'Рабочий тел', 'Личный тел']


class FileCSV:
    NAME_FILE = 'telephone_directory.csv'

    # Чтение из CSV файла
    @classmethod
    def _read(self) -> DataFrame: 
        ''' Считывает данные из файла, добавляя индексы в запись '''
        data = read_csv(self.NAME_FILE)
        data.index = range(1, len(data)+1)
        return data


    @classmethod
    def _write_to_end(self, data: DataFrame) -> None:
        ''' Запись в конец файла CSV '''        
        data.to_csv(self.NAME_FILE, mode='a', header=False, index=False)


    @classmethod
    def _remove_all(self) -> None: 
        ''' Удаляет данные из файла, оставляя наименования колонок первой строкой '''
        with open(self.NAME_FILE, 'wt') as fout:
            csvout = csv.writer(fout)
            csvout.writerow(COLUMNS)
    

    @classmethod
    def _rewrite(self, data: DataFrame) -> None: 
        ''' Перезаписывает CSV файл новыми данными '''
        self._remove_all()
        data.to_csv(self.NAME_FILE, mode='a', header=False, index=False)





