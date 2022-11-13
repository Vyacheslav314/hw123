# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
from seaech_user import data

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Показать всех сотрудников")
    print("7. завершить работу ")
    return int(input("Введите номер необходимого действия: "))


def show_submenu() -> int:
    print("\n" + "=" * 20)
    print("1. Искать сотрудника по id")
    print("2. Искать по ФИО")
    return int(input("Введите номер необходимого действия: "))


def id_num() -> int:
    print("\n" + "=" * 20)
    return int(input("Введите id: "))


def input_user_data():
    print("\n" + "=" * 20)
    my_list = []
    while len(my_list) < 2:
        if len(my_list) == 0:
            my_list.append(input('Введите фамилию '))
        else:
            my_list.append(
                input('Введите имя и отчество если таковое имеется'))
    return my_list


def selection_position():
    print("\n" + "=" * 20)
    return input('Укажите искомую должность ')


def get_salary_renge() -> int:
    print("\n" + "=" * 20)
    print("1. Показать среднюю заработную плату ")
    print("2. Найти все заработные платы ниже средней ")
    print("3. Найти все заработные платы выше средней ")
    return int(input("Введите номер необходимого действия "))


def input_data(data):
    print("\n" + "=" * 20)
    data_list = []
    temp = {}
    temp["id"] = data + 1
    temp["last_name"] = input('Введите Фамилию нового сотрудника: ')
    temp["first_name"] = input('Введите Имя и Отчество нового сотрудника: ')
    temp["position"] = input('Введите должность нового сотрудника: ')
    temp["phone_number"] = input('Введите номер телефона нового сотрудника: ')
    temp["salary"] = float(input('Введите размер заработной платы нового сотрудника: '))
    data_list.append(temp)
    return data_list



