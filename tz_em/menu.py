import os
import sys
import subprocess
from simple_term_menu import TerminalMenu


# Опции меню
MUNE_1 = "1. Поиск записи"
MUNE_2 = "2. Добавить запись"
MUNE_3 = "3. Редактировать записи"
MUNE_4 = "4. Выход"

# Опции подменю_1 (1. Поиск записи)
SUBMUNE_1_1 = "1. По ФИО"
SUBMUNE_1_2 = "2. По Компании"
SUBMUNE_1_3 = "3. По Телефону"
SUBMUNE_1_4 = "4. Показать все записи"
SUBMUNE_1_5 = "5. Назад"

# Опции подменю_3 (3. Редактировать записи)
SUBMUNE_3_1 = "1. Изменить"
SUBMUNE_3_2 = "2. Удалить"
SUBMUNE_3_3 = "3. Удалить все записи"
SUBMUNE_3_4 = "4. Назад"


def menu():
    """
        Вывод меню и выбор пользователем элемента меню
    """
    try:
        while(True):
            subprocess.call("clear", shell=True)
            print(f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
            print(f"\nГлавное меню\n{'-'*30}")
            options_mune = [MUNE_1, MUNE_2, MUNE_3, MUNE_4]
            choice = TerminalMenu(options_mune).show()
            if options_mune[choice] == MUNE_1:
                sub_menu_1()
            elif options_mune[choice] == MUNE_2:
                sub_menu_1()
            elif options_mune[choice] == MUNE_3:
                sub_menu_1()
            elif options_mune[choice] == MUNE_4:
                subprocess.call("clear", shell=True)
                exit()
    except Exception as ex:
        print(ex)
        exit()


def sub_menu_1():
    """
        Вывод подменю первой опции и выбор пользователем элемента подменю
    """
    while(True):
        subprocess.call("clear", shell=True)
        print(f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
        print(f"\nПоиск записи\n{'-'*30}")
        options_submune = [SUBMUNE_1_1, SUBMUNE_1_2, SUBMUNE_1_3, SUBMUNE_1_4, SUBMUNE_1_5]
        choice = TerminalMenu(options_submune).show()
        if options_submune[choice] == SUBMUNE_1_1:
            pass
        elif options_submune[choice] == SUBMUNE_1_2:
            pass
        elif options_submune[choice] == SUBMUNE_1_3:
            pass
        elif options_submune[choice] == SUBMUNE_1_4:
            pass
        elif options_submune[choice] == SUBMUNE_1_5:
            break


def sub_menu_3():
    """
        Вывод подменю третьей опции и выбор пользователем элемента подменю
    """
    while(True):
        subprocess.call("clear", shell=True)
        print(f"ТЕЛЕФОННЫЙ СПРАВОЧНИК")
        print(f"\nРедактировать записи\n{'-'*30}")
        options_submune = [SUBMUNE_3_1, SUBMUNE_3_2, SUBMUNE_3_3, SUBMUNE_3_4]
        choice = TerminalMenu(options_submune).show()
        if options_submune[choice] == SUBMUNE_3_1:
            pass
        elif options_submune[choice] == SUBMUNE_3_2:
            pass
        elif options_submune[choice] == SUBMUNE_3_3:
            pass
        elif options_submune[choice] == SUBMUNE_3_4:
            break


def exit():
    sys.exit(0)
