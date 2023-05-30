PATH = '/Users/malinovskiistan/Desktop/Python/FirstCode/PythonSeminars/Homework/Seminar08_HW/phonebook.txt'

def create_contact():
    name = input('Enter name of contact: ').capitalize()
    mid_name = input('Enter middle name of contact: ').capitalize()
    last_name = input('Enter last name of contact: ').capitalize()
    phone_num = input('Enter phone number of contact: ')
    with open(PATH, 'a', encoding='UTF-8') as file:
        file.write(f'{name};{mid_name};{last_name};{phone_num}\n')
        return f'New contact added'

def show_pb():
    with open(PATH, 'r', encoding='UTF-8') as file:
        ph_book = file.readlines()
    new_book = {}
    for i, j in enumerate(ph_book, 1):
        j = j.strip().split(';')
        new_book[i] = {'Name': j[0], 'Middle name': j[1], 'Last name': j[2], 'Phone': j[3]}
    print(new_book)
        
def find_contact():
    with open(PATH, 'r', encoding='UTF-8') as file:
        ph_book = file.readlines()
    find_value = input('Enter contact to find: ').capitalize()
    new_book = {}
    for i, j in enumerate(ph_book, 1):
        j = j.strip().split(';')
        new_book[i] = {'Name': j[0], 'Middle name': j[1], 'Last name': j[2], 'Phone': j[3]}
    for num, contact in new_book.items():
        for value in contact.values():
            if value == find_value:
                print(new_book[num])

def change_contact():
    with open(PATH, 'r', encoding='UTF-8') as file:
        ph_book = file.readlines()
    find_value = input('Enter contact to change: ').capitalize()
    new_book = {}
    temp = {}
    for i, j in enumerate(ph_book, 1):
        j = j.strip().split(';')
        new_book[i] = {'Name': j[0], 'Middle name': j[1], 'Last name': j[2], 'Phone': j[3]}
    for num, contact in new_book.items():
        for value in contact.values():
            if value == find_value:
                print(new_book[num])
                temp = dict(new_book[num])
    print('1 - Name\n2 - Middle name\n3 - Last name\n4 - Phone')
    change_value = input('What you want to change: ')
    match change_value:
            case '1':
                new_name = input('Enter new Name: ')
                new_book[num]['Name'] = new_name
            case '2':
                new_midname = input('Enter new Middle name: ')
                new_book[num]['Middle name'] = new_midname
            case '3':
                new_lastname = input('Enter new Last name: ')
                new_book[num]['Last name'] = new_lastname
            case '4':
                new_phone = input('Enter new Phone: ')
                temp['Phone'] = new_phone



def delete_contact():
    with open(PATH, 'r', encoding='UTF-8') as file:
        ph_book = file.readlines()
    del_value = input('Enter contact to delete: ').capitalize()
    new_book = {}
    for i, j in enumerate(ph_book, 1):
        j = j.strip().split(';')
        new_book[i] = {'Name': j[0], 'Middle name': j[1], 'Last name': j[2], 'Phone': j[3]}
    for num, contact in new_book.items():
        for value in contact.values():
            if value == del_value:
                new_book.pop(num)


def main_func():
    print('Menu:\n1 - Show phonebook\n2 - Create contact\n3 - Find contact\n4 - Change contact\n5 - Delete contact')
    point = input('Choose your action: ')
    while point:
        match point:
            case '1':
                show_pb()
            case '2':
                create_contact()
            case '3':
                find_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
        point = input('Menu:\n1 - Show phonebook\n2 - Create contact\n3 - Find contact\n4 - Change contact\n5 - Delete contact\nChoose your action (To Exit press "Enter"): ')

main_func()