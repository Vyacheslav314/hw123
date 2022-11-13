import import_data as imd
from tabulate import tabulate


data = imd.read_json()

def search_id(id, data):    
    temp = [] 
    for i in data:
        if i["id"] == id:
            temp.append(i)
    return temp
   
def search_name(name, data):
    temp = [] 
    for i in data:
        if i["first_name"] == name[1] and i["last_name"] == name[0]:
            temp.append(i)
    return temp             

def search_position(position, data):
    temp = [] 
    for i in data:
        if i["position"] == position:
            temp.append(i)
    return temp

def get_middle_salary(data):
    mid = 0
    count = 0
    for i in data:
        count += 1
        mid += i["salary"]
    return round((mid / count), 2)


def selection_salary_min(mid, data) -> list:
    result = []
    for employee in data:
        if mid >= employee["salary"]:
            result.append(employee)
    return result


def selection_salary_max(mid, data) -> list:
    result = []
    for employee in data:
        if mid <= employee["salary"]:
            result.append(employee)
    return result
