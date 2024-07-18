import re


def total_salary(path):
    try:
        pattern = "\d+"
        with open(path, 'r+') as fh:
            salary = fh.readlines()
        total = sum([int(re.search(pattern, i).group()) for i in salary])
        avarage = int(total / len(salary))
        return f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}'
    except (FileExistsError, FileNotFoundError):
        return f'Файл {path} не найден или повреджен, введите коррекный путь или имя файла'


def get_cats_info(path):
    try:
        res = []
        pattern = '\d+'
        with open(path, 'r+') as fh:
            cats = fh.readlines()
        list_cat = [x.split(',') for x in cats]
        for i in list_cat:
            res.append({'id': i[0], 'name': i[1],
                        'age': re.search(pattern, i[2]).group()})
    except (FileExistsError, FileNotFoundError):
        return f'Файл {path} не найден или повреджен, введите коррекный путь или имя файла'
    return res
