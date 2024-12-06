

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(a, b, n=", "):
    list_a = a.split('|')   # перечисление участников без разделителей
    list_b = b.split('|')
    common_participants = set(list_a).intersection(set(list_b))   # отбор общих участников среди двух групп
    list_common_participants = list(common_participants)   # преобразование множества в список для сортировки
    list_common_participants.sort()   # сортировка списка в алфавитном порядке
    result = n.join(list_common_participants)
    return result   # вывод отсортированного списка общих участников

print(find_common_participants(participants_first_group, participants_second_group))   # вызов функции

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, n="! "))



def find_common_participants_(a, b, n=", "):
    list_a = a.split('|')   # перечисление участников без разделителей
    list_b = b.split('|')
    common_participants = set(list_a).intersection(set(list_b))   # отбор общих участников среди двух групп
    list_common_participants = list((common_participants))   # преобразование множества в список для сортировки
    list_common_participants.sort()   # сортировка списка в алфавитном порядке
    result = (n.join(list_common_participants)).split()
    return(result)      # вывод отсортированного списка общих участников

print(find_common_participants_(participants_first_group, participants_second_group))   # вызов функции

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants_(participants_first_group, participants_second_group, n="! "))
