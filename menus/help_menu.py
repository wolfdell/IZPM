# Imports for the class
from menus.menu import Menu
from util.flush import flush_screen

class HelpMenu(Menu):

    # Create the menu instance
    def spawn(self):

        # Clear the screen
        flush_screen()

        # Print the menu
        print('\x1b[6;30;42m' + ' Меню за помощ ' + '\x1b[0m')
        print("'\x1b[0;36;40mнов превод\x1b[0m'        - стартира меню за нов превод")
        print("'\x1b[0;36;40mпокажи превод <х>\x1b[0m' - показва информация за съответната глава")
        print("'\x1b[0;36;40mпокажи всички\x1b[0m'     - показва всички преводи, направени в настоящата сесия")
        print("'\x1b[0;36;40mизход\x1b[0m'             - спира изпълнението на програмата")
        
        # Add an empty line
        print()