
from logger import input_data, print_data, change_data, delete_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GB \n 1 - запись данных \n 2 - вывод данных \n 3 - изменить данные \n 4 - удалить данные")
    command = int(input('Введите число: '))
    

    while command != 1 and command != 2 and command != 3 and command !=4 :
        print("Неправильный ввод")
        command = int(input('введите число: '))

    if command == 1 :
        input_data()
    elif command == 2 :
        print_data()
    elif command == 3 :
        change_data()
    elif command == 4 :
        delete_data()

interface()