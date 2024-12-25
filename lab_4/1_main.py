# TODO решите задачу
def task(file_name) -> float:
    import json

    with open(file_name) as f:
        my_dict = json.load(f)
        score = [dict['score'] for dict in my_dict]
        weight = [dict['weight'] for dict in my_dict]
        help_dict = []

        for i in range(len(score)):
            help_dict.append(score[i] * weight[i])
        c = round(sum(help_dict), 3)

        return print(c)

task('input.json')


