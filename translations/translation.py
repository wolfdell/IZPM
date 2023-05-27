import math
from util.flush import flush_screen

class Translation:
    # Тази функция създава файловото име
    def create_file_name(self):
        filename = f"{self.get_translator()}_{self.get_name()}_vol-{self.add_leading_zeros(self.get_volume(), 2)}_ch-{self.add_leading_zeros(self.get_chapter(), 3)}.{self.get_extension()}"
        return filename

    def add_leading_zeros(self, number, zeros):
        if len(str(number)) < zeros:
            # {:03d}
            # 02d
            query = f":0{abs(int(zeros) - len(str(number)))}d"
            query = '{' + query + '}'
            return f"{query.format(int(number))}"
        elif len(str(number)) > zeros:
            return number
        else:
            return number

    def metadata_out(self):
        flush_screen()
        print("\n\x1b[6;30;42m Метаданни за този превод \x1b[0m")
        print("---------------------------")
        print("За мангата: ")
        print(f"Име на мангата:\t \x1b[0;36;40m{self.get_name()}\x1b[0m")
        print(f"Настоящ том:\t \x1b[0;36;40m{self.get_volume()}\x1b[0m")
        print(f"Настояща глава:\t \x1b[0;36;40m{self.get_chapter()}\x1b[0m")
        print("\nЗа превода: ")
        print(f"Преводач:\t \x1b[0;36;40m{self.get_translator()}\x1b[0m")
        print(f"Редактор:\t \x1b[0;36;40m{self.get_editor()}\x1b[0m")
        print(f"Моделиране:\t \x1b[0;36;40m{self.get_typesetter()}\x1b[0m")
        print(f"\nФайлово име:\t \x1b[0;36;40m{self.get_filename()}\x1b[0m")
        print(f"Екстеншън:\t \x1b[0;36;40m.{self.get_extension()}\x1b[0m")

    # Тези нека стоят най-отдолу, за да не пречат
    # Гетъри и сетъри с цел сигурност. Моля, ако някой работи по проекта да ползва само тях за достъп
    def manga_name_setter(self, manga_name):
        name_tokens = manga_name.split()
        manga_name = "_".join(name_tokens)
        self.manga_name = manga_name.lower()

    def manga_volume_setter(self, manga_volume):
        self.manga_volume = manga_volume

    def manga_chapter_setter(self, manga_chapter):
        self.manga_chapter = manga_chapter

    def manga_translator_setter(self, manga_translator):
        self.manga_translator = manga_translator.lower()

    def manga_editor_setter(self, manga_editor):
        self.manga_editor = manga_editor.lower()

    def manga_typesetter_setter(self, manga_typesetter):
        self.manga_typesetter = manga_typesetter.lower()

    def manga_filename_setter(self, manga_filename):
        self.manga_filename = manga_filename

    def manga_extension_setter(self, manga_extension):
        self.manga_extension = manga_extension.lower()

    def get_name(self):
        return self.manga_name
    
    def get_volume(self):
        return self.manga_volume

    def get_chapter(self):
        return self.manga_chapter

    def get_translator(self):
        return self.manga_translator

    def get_editor(self):
        return self.manga_editor

    def get_typesetter(self):
        return self.manga_typesetter
    
    def get_filename(self):
        return self.manga_filename

    def get_extension(self):
        return self.manga_extension

    def __init__(self, name, volume, chapter, translator, editor, typesetter, extension):
        self.manga_name_setter(name)
        self.manga_volume_setter(volume)
        self.manga_chapter_setter(chapter)
        self.manga_translator_setter(translator)
        self.manga_editor_setter(editor)
        self.manga_typesetter_setter(typesetter)
        self.manga_extension_setter(extension)
        self.manga_filename_setter(self.create_file_name())