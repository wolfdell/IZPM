# Imports for the class
from menus.menu import Menu
from util.flush import flush_screen
from util.translation_holder import TranslationHolder

# TODO: За реализацията на това меню трябва да се довърши и translation holder класа
class TranslationInfoMenu(Menu):

    def __init__(self):

        # Translation index holder
        self.index = None

    # Create the menu instance
    def spawn(self):
        pass