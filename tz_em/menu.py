import sys
from subprocess import call
from pandas import DataFrame

from simple_term_menu import TerminalMenu

from service import get_entry_data, get_all_data, get_interval_data
from service import add_entry_data, del_all_data, del_entry_data, updata_entry_data


# Опции меню
MUNE_1 = "1. Поиск записи"
MUNE_2 = "2. Добавить запись"
MUNE_3 = "3. Редактировать записи"
MUNE_4 = "4. Выход"

# Опции подменю_1 (1. Поиск записи)
SUBMUNE_1_1 = "1. Найти по совпадению"
SUBMUNE_1_2 = "2. Показать все записи"
SUBMUNE_1_3 = "3. Назад"

# Опции подменю_3 (3. Редактировать записи)
SUBMUNE_3_1 = "1. Изменить запись"
SUBMUNE_3_2 = "2. Удалить запись"
SUBMUNE_3_3 = "3. Удалить все записи"
SUBMUNE_3_4 = "4. Назад"

# Пагинация 
PAGINATION_START = 0
PAGINATION_STEP = 10

SUBMUNE_0_1 = f" Следующии {PAGINATION_STEP}"
SUBMUNE_0_2 = f" Предыдущии {PAGINATION_STEP}"
SUBMUNE_0_3 = " Назад"


# ГЛАВНОЕ МЕНЮ
def menu() -> None:
    ''' Вывод меню и выбор пользователем элемента меню '''
    try:
        while(True):
            title('Главное меню')  
            options_mune = [MUNE_1, MUNE_2, MUNE_3, MUNE_4]
            choice = TerminalMenu(options_mune).show()
            if options_mune[choice] == MUNE_1: # Поиск записи
                sub_menu_1()
            elif options_mune[choice] == MUNE_2: # Добавить запись
                result_ = add_entry_data()
                if result_:
                    result_func('Запись добавлена')
                else:
                    result_func('Запись не добавлена')
            elif options_mune[choice] == MUNE_3: # Редактировать записи
                sub_menu_3()
            elif options_mune[choice] == MUNE_4: # Выход
                call("clear", shell=True)
                sys.exit(0)
    except Exception as ex:
        print(ex)
        sys.exit(0)


# ПОДМЕНЮ
# Меню поиска записей в телефонной книге
def sub_menu_1() -> None:
    ''' Вывод подменю первой опции и выбор пользователем элемента подменю '''
    while(True):
        title('Поиск записи')  

        options_submune = [SUBMUNE_1_1, SUBMUNE_1_2, SUBMUNE_1_3]
        choice = TerminalMenu(options_submune).show()

        if options_submune[choice] == SUBMUNE_1_1: # Найти запись по совпадению
            data = get_entry_data()
            if not data.empty:
                pagination_menu(data, PAGINATION_START, PAGINATION_STEP)
            else:
                result_func('Запись не найдена')
        elif options_submune[choice] == SUBMUNE_1_2: # Показать все записи  
            data = get_all_data()
            if not data.empty:
                pagination_menu(data, PAGINATION_START, PAGINATION_STEP)
            else:
                result_func('Записи не найдены')
        elif options_submune[choice] == SUBMUNE_1_3:
            break


# Меню редактирования телефонной книги
def sub_menu_3() -> None:
    ''' Вывод подменю третьей опции и выбор пользователем элемента подменю '''
    while(True):
        title('Редактировать записи')  

        options_submune = [SUBMUNE_3_1, SUBMUNE_3_2, SUBMUNE_3_3, SUBMUNE_3_4]
        choice = TerminalMenu(options_submune).show()

        if options_submune[choice] == SUBMUNE_3_1: # изменить запись
            result_ = updata_entry_data()
            if result_:
                result_func('Запись изменена')
            else:
                result_func('Запись не изменена')
        elif options_submune[choice] == SUBMUNE_3_2: # удалить запись по индексу
            result_ = del_entry_data()
            if result_:
                result_func('Запись удалена')
            else:
                result_func('Запись не удалена')
        elif options_submune[choice] == SUBMUNE_3_3: # удалить все записи
            result_ = del_all_data()
            if result_:
                result_func('Записи удалены')
            else:
                result_func('Записи не удалены')
        elif options_submune[choice] == SUBMUNE_3_4: # назад
            break


# ПАГИНАЦИЯ
def pagination_menu(data: DataFrame, start_index: int, end_index: int) -> None:
    ''' Пагинация по страницам поиска телефонных контактов '''
    title('Поиск записи')

    len_ = len(data)
    if end_index > len_:
        end_index = len_
    get_interval_data(data, start_index, end_index)

    while(True):
        print(f"\nПеремещение\n{'-'*30}")

        if start_index == PAGINATION_START and end_index == len_:
            options_submune = ['1.' + SUBMUNE_0_3]
        elif start_index == PAGINATION_START:
            options_submune = ['1.' + SUBMUNE_0_1, '2.' + SUBMUNE_0_3]
        elif end_index >= len_:
            options_submune = ['1.' + SUBMUNE_0_2, '2.' + SUBMUNE_0_3]
        else:
            options_submune = ['1.' + SUBMUNE_0_1, '2.' + SUBMUNE_0_2, '3.' + SUBMUNE_0_3]

        choice = TerminalMenu(options_submune).show()

        if options_submune[choice][2:] == SUBMUNE_0_1:
            start_index, end_index = pagination_next(start_index, end_index, PAGINATION_STEP, len_)
            get_interval_data(data, start_index, end_index)
        elif options_submune[choice][2:] == SUBMUNE_0_2:
            start_index, end_index = pagination_previous(start_index, end_index, PAGINATION_STEP, PAGINATION_START)
            get_interval_data(data, start_index, end_index)
        elif options_submune[choice][2:] == SUBMUNE_0_3:
            break


def pagination_next(start: int, end: int, step: int, len: int) -> None:
    ''' Пагинация: следующая страница '''
    title('Поиск записи')
       
    if end >= len: 
        end == len
        return start, end    
    start, end = end, end + step 
    return start, end


def pagination_previous(start: int, end: int, step: int, beginning: int) -> None:
    ''' Пагинация предыдущая страница '''
    title('Поиск записи')

    start, end = start - step, start
    if start < beginning:
        start, end = beginning, step
    return start, end


def title(title_: str):
    ''' Заголовок программы для вывода в терминал '''
    call("clear", shell=True)
    print(f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print(f"\n{title_}\n{'-'*30}")


def result_func(result_: str):
    ''' Результат работы функции для вывода в терминал '''
    print(f'\n{result_}\n')
    input("Нажмите 'Enter' чтобы вернуться назад")
