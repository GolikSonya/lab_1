# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(a) -> None:
    ...  # TODO считать содержимое csv файла
    import csv
    with open(a) as f:
        lines = [line for line in csv.DictReader(f)]



    ...  # TODO Сериализовать в файл с отступами равными 4
    import json
    with open(OUTPUT_FILENAME, 'w') as o:
        json.dump(lines, o, indent=4)


task(INPUT_FILENAME)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
