from pprint3x import pprint
from decorators import logger
from datetime import datetime
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
@logger
def template_list(work_list):
    result = [[]]
    for stroke in work_list:
        for index in range(len(stroke)):
            if stroke[index] != '' and index <= 2:
                res = re.split(r'\W', stroke[index])
                for i in range(len(res)):
                    result[-1].append(res[i])
            elif len(result[-1]) < 3:
                result[-1].append('')
            elif index == 5:
                pattern = r'(\+7|8)[\s(]*(\d{3})[\s)-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s(]*(доб.)*[\s]*(\d{4})*[)]*'
                repl = r'+7(\2)\3-\4-\5 \6\7'
                result[-1].insert(index, (re.sub(pattern, repl, stroke[index])))
            elif index in (3, 4, 6):
                result[-1].insert(index, (stroke[index]))
        result.append([])
    result.pop(0)
    result.pop()
    return result


formatted_list = template_list(contacts_list)


def create_list_to_write(source_list):
    write_list = []
    person_list = []
    for person in source_list:
        if not person_list:
            person_list.append(person[0])
            write_list.append(person)
        elif person[0] not in person_list:
            person_list.append(person[0])
            write_list.append(person)
        elif person[0] in person_list:
            for write in write_list:
                if person[0] == write[0] and person[1] == write[1]:
                    for i in range(len(person)):
                        if write[i] == '' and person[i] != '':
                            write[i] = person[i]
    return write_list


ready_write_list = create_list_to_write(formatted_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(ready_write_list)

