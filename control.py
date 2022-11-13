import intrface as inter
import seaech_user as sea_us
from tabulate import tabulate
import import_data as imd
import create

is_valid = True
while is_valid:
    command = inter.show_menu()
    if command == 1:
        temp = inter.show_submenu()
        if temp == 1:
            print(tabulate(sea_us.search_id(inter.id_num(), imd.read_json())))
        elif temp == 2:
            print(tabulate(sea_us.search_name(inter.input_user_data(), imd.read_json())))
    elif command == 2:
        print(tabulate(sea_us.search_position(
            inter.selection_position(), imd.read_json())))
    elif command == 3:
        temp = inter.get_salary_renge()
        mid_salary = sea_us.get_middle_salary(imd.read_json())
        if temp == 1:
            print(f'\nСредняя заработная плата по компании = {mid_salary}')
        elif temp == 2:
            print(tabulate(sea_us.selection_salary_min(mid_salary, imd.read_json())))
        elif temp == 3:
            print(tabulate(sea_us.selection_salary_max(mid_salary, imd.read_json())))
    elif command == 4:
        id_num = len(imd.read_json())
        add_user = inter.input_data(id_num)
        print(tabulate(create.add_csv(add_user)))
        print(tabulate(create.add_json(add_user)))
    elif command == 5:
        data = data = imd.read_json()
        data_id = inter.id_num()

        def delete_data(data, data_id):
            my_list = []
            for i in data:
                if i["id"] != data_id:
                    my_list.append(i)
            return my_list
        create.write_csv(delete_data(data, data_id))
        create.write_json(delete_data(data, data_id))
    elif command == 6:
        print(tabulate(imd.read_json()))
    elif command == 7:
        is_valid = False
    else:
        print("нет такой команды")