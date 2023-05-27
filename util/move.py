# Функция за преместване на настоящия файл в друга папка
def choose_translation_path(file):
    print('\x1b[6;30;42m' + ' Моля, изберете къде да запазите превода ' + '\x1b[0m')
    print("По подразбиране папката е настоящата")
    path = input("Посочете папка: ")

    if path.strip() == "":
        pass

    current = f"{file}"

    shutil.move(current, path)
    print("Файлът беше преместен успешно")
