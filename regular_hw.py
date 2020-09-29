from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ

def telephone_convertor(telephone_string):
    new_string = ''
    for letter in telephone_string:
        if letter.isnumeric():
            new_string = new_string + letter
    new_string = '+7' + '(' + new_string[1:4] + ')' \
                 + new_string[4:7] + '-' + new_string[7:9] + '-' + new_string[9:11]
    return new_string


pattern = r"(^[А-Яа-я]+)(,*| *)([А-Яа-я]+)(.)(([А-Яа-я]+)|())(,*)(([А-Яа-я]+)|())(,*)(([а-яa-zА-Я ]+\W[а-яa-zА-Я " \
          r"]+)|([а-яa-zА-Я ]+)|())(,*)((\W)|())((\d\D{1,3}\d{3}\D{1,3}\d+\D\d+((\d+)|(\D\d+)))|(\d+)|())((\D+доб\D+[" \
          r"0-9]+)|())((\W{1,2})|())(([0-9A-Za-z((.)|())]+@\w+.\w+)|())"
# pattern = re.compile(pattern)

new_list = []
for element in contacts_list:
    # print(element)
    str_element = ",".join(element)
    result = re.search(pattern, str_element)
    if result is not None:
        new_dict = {}
        new_dict['lastname'] = result[1]
        new_dict['firstname'] = result[3]
        if result[6] is not None:
            new_dict['surname'] = result[6]
        if result[10] is not None:
            new_dict['organization'] = result[10]
        if result[14] is not None:
            new_dict['position'] = result[14]
        if len(result[21]) > 1:
            if result[29] is not None:
                add_number = ' доб.' + result[29][-4:-1] + result[29][-1]
                new_dict['phone'] = telephone_convertor(result[21]) + add_number
            else:
                new_dict['phone'] = telephone_convertor(result[21])
        if result[35] is not None:
            new_dict['email'] = result[35]

        new_list.append(new_dict)
pprint(new_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "a") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_list)
