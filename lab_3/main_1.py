# TODO Напишите функцию для поиска индекса товара

def find(list,fruit):
    if fruit in list:                # условие: есть ли товар в списке?
        index = list.index(fruit)    # если да - присваиваем индекс
    else:
        index = None                 # если нет - присваиваем none
    return(index)                    # выводим значение индекса товара

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

