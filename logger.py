
from data_create import name_data, surname_data, phone_data, address_data

def  input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var  = int(input(
        f'Which variant  want to use?\n\n1 variant:\n{name}\n{surname}\n{phone}\n{address}\n\n'
        f'2 variant: \n{name};{surname};{phone};{address}\n select your variant to record (1 or 2): '))


    while  var != 1 and var != 2:
        print("incorrect input ")
        var = int(input('Input number: '))         

    if var == 1:
        with open('data_first_variant.csv', 'a' , encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
            #return f'{name}\n{surname}\n{phone}\n{address}\n\n'

    
    elif var == 2:
        with open('data_second_variant.csv', 'a' , encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")
            #return f'{name};{surname};{phone};{address}\n'

        


def print_data():
    command = int(input('write which file you want to read(1/2): '))

    while command != 1 and command != 2:
        print('Wrong command')
        command = int(input('Enter command: '))

    if command == 1:
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_variant.csv', 'r' , encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == "\n" or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i
            print(''.join(data_first_list))
            return data_first
    elif command == 2:
        print('Вывожу данные из 2 файла: \n')
        with open('data_second_variant.csv', 'r' , encoding='utf-8') as f:
            data_second = f.readlines()
            print(*data_second)
            return data_second

def change_data():
    data_list = print_data()
    name_data_d = input('input  name  you want to change: ')
    number_file = int(input('input number of file you want change(1/2): '))
    while number_file not in [1, 2]:
        print('Wrong number_file')
        number_file = int(input('input number of file you want change(1/2): '))
    
    file_name = f'data_first_variant.csv' if number_file == 1 else f'data_second_variant.csv'
    
    with open(file_name, 'w', encoding='utf-8') as f:
            for i, line in enumerate(data_list):
                if str(line).startswith(name_data_d):
                    data_list[i] = input_data()
                f.write(str(data_list[i]))


def delete_data():
    data_list = print_data()
    name_data_d = input('input name  you want to delete: ')
    number_file = int(input('input  number of  file you want to delete in(1/2): '))
    while number_file != 1 and number_file != 2:
        print('Wrong number_file')
        number_file = int(input('input  number of  file you want to delete in(1/2): '))
    if number_file == 1:
            with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                for i in range(len(data_list)):
                    if not str(data_list[i]).startswith(name_data_d):
                        f.write(str(data_list[i]))
                        
    elif number_file == 2:
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    f.write(str(*data_list[:i]))
                    f.write(str(*data_list[i + 1:]))
                        


   




   
    
