# Imports for the class
from menus.menu import Menu
from util.flush import flush_screen

from translation_utils.translation import Translation

class NewTranslationMenu(Menu):
    

    # Create the menu instance
    def spawn(self):
        
        # Fetch the information about the team
        translator_name, editor_name, typesetter_name = self.get_manga_team()

        # Fetch the information about the translation
        manga_name, manga_chapter, manga_volume, team = self.get_manga_info()

        # Fetch information about the extension
        extention_name = self.get_extention()

        # Create the current translation instance
        translation = Translation(manga_name, manga_volume, manga_chapter, translator_name, redactor_name, typesetter_name, extention_name)

        # TODO: тук е момента, в който трябва да добавим новия превод към колекцията с готови преводи

        # TODO: Проблем при инициализирането на пътя, трябва да отваря папката и файла, но не ги създава.
        file_name = translation.create_file_name()

        # Print the file name
        print("\x1b[0;36;40m[+]\x1b[0m В този случай, името на файла ще бъде:", '\x1b[0;36;40m' + file_name + '\x1b[0m\n')

        # Check if we want to continue to the translation session
        check = input("Да продължим ли към сесията за превод \x1b[0;36;40m[да/не]\x1b[0m: ")
        if check.lower() == "да":
            translation_session(file_name, translator_name, editor_name, typesetter_name)
        else:
            print("Добре, значи днес няма да превеждаме...\n")

    def translation_session(file_name, translator_name, editor_name, typesetter_name):
        
        # TODO:

        pass

    # Method to get the manga extention
    def get_extention():
        return input("Какъв искате да бъде екстеншъна на мангата: ")

    # Method to get information about the manga
    def get_manga_info():

        # Clear the screen
        flush_screen()

        # Print the menu title
        int('\x1b[6;30;42m' + ' Нека разбера малко още за превода ' + '\x1b[0m')

        # Get information about the manga
        manga_name      = input("Името на мангата: ")
        manga_chapter   = input("Главата: ")
        manga_volume    = input("Том: ")
        team            = input("Преводаческа група: ")

        return manga_name, manga_chapter, manga_volume, team

    # Method to get information about the team
    def get_manga_team(self):
        
        # Clear the screen
        flush_screen()

        # Print menu title
        print('\x1b[6;30;42m' + ' Кажи ми малко за екипа ' + '\x1b[0m')

        # Questions about the translation team
        translator_name = input("Име на преводача: ")
        editor_name     = input("Име на редактора: ")
        typesetter_name = input("Име на тайпсетъра: ")

        # TODO: Functionality to check if all three are equal

        return translator_name, editor_name, typesetter_name 

