import csv
import json
from pathlib import Path
import intrface as inter

def write_csv(employees):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')

def add_csv(employees):
    with open(Path.cwd() / 'database.csv', 'a', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())
            
def add_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'a', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')
            
