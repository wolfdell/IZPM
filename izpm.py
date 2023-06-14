
# Utility imports
from translation_utils.translation import Translation
from util.flush import flush_screen
from util.move import choose_translation_path

# Translation menu imports
from menus.showall_menu import ShowAllMenu
from menus.help_menu import HelpMenu
from menus.comment_menu import CommentSectionMenu

# Python source imports
import os
import shutil
import keyboard

# Translation holder (current state)
translations = []

# Menus initialization
show_all_menu   = ShowAllMenu()
help_menu       = HelpMenu()
comment_menu    = CommentSectionMenu()

def new_translation():
    translator_name, redactor_name, typesetter_name = get_manga_name()
    manga_name, manga_chapter, manga_volume, translators = get_manga_info()
    extention_name = input("Какъв искате да бъде екстеншъна на мангата: ")

    translation = Translation(manga_name, manga_volume, manga_chapter, translator_name, redactor_name, typesetter_name, extention_name)
    translations.append(translation)

    # TODO: Проблем при инициализирането на пътя, трябва да отваря папката и файла, но не ги създава.
    file_name = translation.create_path() + self.create_file_name()

    print("\x1b[0;36;40m[+]\x1b[0m В този случай, името на файла ще бъде:", '\x1b[0;36;40m' + file_name + '\x1b[0m')
    print()
    to_continue = input("Да продължим ли към сесията за превод \x1b[0;36;40m[да/не]\x1b[0m: ")
    if to_continue.lower() == "да":
        translation_period(file_name, translator_name, redactor_name, typesetter_name)
    else:
        print("Добре, значи днес няма да превеждаме...")
        print()


def translation_period(file_name, translator, editor, typesetter):
    flush_screen()
    print('\x1b[6;30;42m' + ' Настояща сесия за превод ' + '\x1b[0m')
    print("------------------\n\rЗа работа с програмата:\n\r\x1b[0;36;40m+\x1b[0m - нова страница\n\r\x1b[0;36;40mq\x1b[0m - изход\n\r")

    page = 1
    panel = 1
    add_comment = False

    with open(file_name, "a") as f:
        print("Превод на нова глава\n", file=f)
        while True:
            line = input('\x1b[0;36;40m' + f"[стр. {page}/ поле {panel}] /> " + '\x1b[0m')

            if keyboard.is_pressed('+'):
                print("", file=f)
                page += 1
                panel = 1
                continue

            if line.strip() == "":
                continue

            if line == "q":
                check = input("Сигурни ли сте, че искате да приключите с превода \x1b[0;36;40m[да/не]\x1b[0m: ")
                if check.lower() == "да":
                    print()
                    print("\x1b[0;36;40m[+]\x1b[0m Успешно завършихте своя превод")

                    print("----------", file=f)
                    print()
                    print(f"Преводач: {translator}", file=f)
                    print(f"Редактор: {editor}", file=f)
                    print(f"Тайпсетър: {typesetter}", file=f)
                    c_com = input("Искате ли да добавите коментар към своя превод \x1b[0;36;40m[да/не]\x1b[0m: ")
                    if c_com.lower() == "да":
                        add_comment = True
                    break

            print(f"[стр. {page}/ пан. {panel}]: {line}", file=f)
            panel += 1

    # Check for the comment menu command
    if add_comment:
        
        # Set the translation holder to the file name
        comment_menu.translation_file = file_name

        # Spawn the comment menu instance
        comment_menu.spawn()

def show_translation(index):
    translations[index - 1].metadata_out()
    print()

def get_manga_info():
    flush_screen()
    print('\x1b[6;30;42m' + ' Нека разбера малко още за превода ' + '\x1b[0m')
    manga_name = input("Името на мангата: ")
    manga_chapter = input("Главата: ")
    manga_volume = input("Том: ")
    translators = input("Преводаческа група: ")

    return manga_name, manga_chapter, manga_volume, translators

def get_manga_name():
    flush_screen()
    print('\x1b[6;30;42m' + ' Кажи ми малко за екипа ' + '\x1b[0m')
    translator_name = input("Име на преводача: ")
    redactor_name = input("Име на редактора: ")
    typesetter_name = input("Име на тайпсетъра: ")

    #if translator_name == redactor_name and redactor_name == typesetter_name:
        #is_one_person = input("Да разбирам ли, че само един човек работи върху превода[да/не]: ") 

    return translator_name, redactor_name, typesetter_name

def show_all():
    flush_screen()
    print('\x1b[6;30;42m' + ' Преводи в настоящата сесия ' + '\x1b[0m')
    
    for id, val in enumerate(translations):
        print(f"Индекс \x1b[0;36;40m<{id + 1}>\x1b[0m -> {val.get_name()}, Глава: {val.get_chapter()}")
    
    print()


if __name__ == '__main__':
    flush_screen()
    print('\x1b[6;30;42m' + 'IZPM версия 0.1' + '\x1b[0m' + "\n\rИзползвайте командата 'помощ' при нужда!")
    
    while True:
        cmd = input("\x1b[0;36;40mМеню: \x1b[0m")
        cmd = cmd.lower()

        # Show the help menu
        if cmd == "помощ":
            help_menu.spawn()
        
        
        if cmd == "изход":
            flush_screen() 
            break
        if cmd == "нов превод": new_translation()
        
        # Show all translations
        if cmd == "покажи всички":
            show_all_menu.spawn()

        if "покажи превод" in cmd:
            tokens = cmd.split()
            show_translation(int(tokens[2]))

#
#   == IZPM source code ==
#      wolfdell @ 2023
#