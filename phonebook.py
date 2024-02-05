import os

def add_new_ser(name:str, phone: str, filename :str):
    with open(filename, 'r+t', encoding='utf-8') as writer:
        lineCount = len(writer.readlines())
        writer.write(f"{lineCount + 1};{name};{phone}\n")

def read_all(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as data:
        result = data.read()
    return result        

def search_user(data: str, filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as content:
        text = content.readlines()
    res =  ([item for item in text if data.lower() in item.lower()])

    return ''.join(res) if res else "Ни чего не найдено"

def check_directory(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write("")

def initDataForCopyFile(filename: str):
    if filename not in os.listdir():
        with open(filename, 'w', encoding='utf-8') as data:
            data.write("1;Test contant 1; +711111111\n")
            data.write("2;Test contant 2; +722222222\n")
            data.write("3;Test contant 3; +733333333\n")
            data.write("4;Test contant 4; +744444444\n")

def copy_contact(num_line: int, filename_from: str, filename_to: str):
    with open(filename_from, 'r', encoding='utf-8') as content, open(filename_to, "r+t", encoding='utf-8') as writer:
        text = content.readlines()
        if(num_line <= len(text)):
            copy_line = text[num_line - 1]
            writer.readlines()
            writer.write(f"\n{copy_line}")

INFO_STRING = """
Выберите режим работы:
1 - Вывести все данные
2 - Добавить нового пользователя
3 - Поиск
4 - Скопировать из одного справочника в другой
5 - Выход
"""

DATASOURCE = 'phone.txt'
DATASOURCECOPY = 'phoneCopyFrom.txt'

check_directory(DATASOURCE)
initDataForCopyFile(DATASOURCECOPY)

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
        user = input("Введите Имя контакта:\n")
        phone = input("Введите Телоефон:\n")
        add_new_ser(user, phone, DATASOURCE)
    elif mode == 3:
        search = input("Введите строку для поиска:\n")
        print(search_user(search, DATASOURCE))
    elif mode == 4:
         print(read_all(DATASOURCECOPY))
         line_num = int(input("Ввидите номер строки из списка выше которую хотите скопировать\n"))
         if line_num >= 1 :
            copy_contact(line_num, DATASOURCECOPY, DATASOURCE)
         else:
            print("Нужно ввести число больше 0")
    elif mode == 5:
        break