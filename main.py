import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

''' Первое задание '''

for human in contacts_list:
    for idx in range(0, 3):
        lfc = human[idx].split(" ")
        match len(lfc):
            case 1:
                continue
            case 2:
                if idx == 0:
                    human[0] = lfc[0]
                    human[1] = lfc[1]
                else:
                    human[1] = lfc[0]
                    human[2] = lfc[1]
            case 3:
                human[0] = lfc[0]
                human[1] = lfc[1]
                human[2] = lfc[2]

''' Второе задание '''

for number in contacts_list:
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?\s*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
    pattern2 = r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?\s*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(\s*\(?\bдоб\.?\s*(\d+)\)?)?"
    number[-2] = re.sub(pattern, r"+7(\2)\3-\4-\5", number[-2])
    if len(number[-2]) > 16:
        number[-2] = re.sub(pattern2, r"+7(\2)\3-\4-\5 доб.\7", number[-2])

''' Третье задание '''
index = []

for index_one, human in enumerate(contacts_list):
    for index_two, next_human in enumerate(contacts_list):
        if human[0] == next_human[0]:
            if index_one == index_two:
                continue
            else:
                if human[1] == next_human[1]:
                    for idx in range(0, 7):
                        if contacts_list[index_one][idx] == contacts_list[index_two][idx]:
                            continue
                        elif contacts_list[index_one][idx] == '':
                            if contacts_list[index_two][idx] != '':
                                contacts_list[index_one][idx] = contacts_list[index_two][idx]
                    del contacts_list[index_two]
print(index)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
