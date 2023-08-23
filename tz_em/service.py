# Файл обработки и выдачи данный
from subprocess import call
from pandas import DataFrame 
from dao import file_csv, COLUMNS


def get_all_data() -> DataFrame:
    ''' Получить все записи справочника '''
    return file_csv._read()


def get_interval_data(data: DataFrame, start_index: int, end_index: int) -> None:
    ''' Получить интервал телефонного справочник '''
    print(data[start_index:end_index].to_markdown())


def get_entry_data() -> DataFrame:
    ''' Найти запись (одну или более) по введённым данным в телефонном справочнике '''
    print('\nВведите известные вам данные или пропустите ввод нажав "Enter"')
    find_entry = input_data_entry()
    dFilter = get_all_data()
    Flag = False

    for col in COLUMNS:
        if find_entry.loc[0, col] != '':
            dFilter = dFilter[dFilter.loc[:,col] == find_entry.loc[0, col]]
            Flag = True
    
    if Flag and not dFilter.empty:
        return dFilter
    return DataFrame()


def del_all_data() -> bool:
    ''' Удалить все записи справочника '''
    file_csv._remove_all()
    return True



def del_entry_data() -> bool:
    ''' Удалить запись справочника '''
    data = get_all_data()
    len_ = len(data)

    del_index = int(input(f"Выберите номер записи от 1 до {len_}: "))
    data = data[data.index != del_index] 

    file_csv._rewrite(data)
    return True



def updata_entry_data() -> bool:
    ''' Изменить запись '''
    data = get_all_data()
    len_ = len(data)

    upd_index = int(input(f"Выберите номер записи от 1 до {len_}: "))
    upd_column = int(input(f"Выберите колонку записи:\
        \n1. Фамилия\
        \n2. Имя\
        \n3. Отчество\
        \n4. Компания\
        \n5. Рабочий тел\
        \n6. Личный тел\n"))
    updata = input(f"Заменить на: ")

    data.iat[upd_index - 1, upd_column - 1] = updata
    file_csv._rewrite(data)
    return True


def add_entry_data() -> bool:
    ''' Добавить запись в конец телефонного справочника '''   
    call("clear", shell=True)
    print(f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(f"\nДобавление записи\n{'-'*30}")

    entry = input_data_entry()

    file_csv._write_to_end(entry)
    return True
    

def input_data_entry() -> DataFrame:
    ''' Ввод данных записи через консоль '''
    surname = input('Фамилия: ')
    name = input('Имя: ')
    patronymic = input('Отчество: ')
    company = input('Компания: ')
    work_phone = input('Рабочий тел: ')
    personal_phone = input('Личный тел: ')

    entry = [
        [surname, name, patronymic, company, work_phone, personal_phone]
    ]
    entry = DataFrame(entry)
    entry.columns = COLUMNS

    return entry

