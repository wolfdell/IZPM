# Imports for the class
from menus.menu import Menu
from util.flush import flush_screen

class ShowAllMenu(Menu):

    # Create the menu instance
    def spawn(self):

        # Clear the screen
        flush_screen()

        # Print the information on the screen
        print('\x1b[6;30;42m' + ' Преводи в настоящата сесия ' + '\x1b[0m')
    
        for id, val in enumerate(translations):
            print(f"Индекс \x1b[0;36;40m<{id + 1}>\x1b[0m -> {val.get_name()}, Глава: {val.get_chapter()}")
    
        # Add empty line after
        print()