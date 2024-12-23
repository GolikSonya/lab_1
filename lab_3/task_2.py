



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(a, b, n=","):
    list_a = a.split(n)   # перечисление участников без разделителей
    list_b = b.split(n)
    common_participants = set(list_a).intersection(set(list_b))   # отбор общих участников среди двух групп
    list_common_participants = list(common_participants)   # преобразование множества в список для сортировки
    list_common_participants.sort()   # сортировка списка в алфавитном порядке
    return list_common_participants   # вывод отсортированного списка общих участников

print(find_common_participants(participants_first_group, participants_second_group, n="|"))   # вызов функции

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group))
