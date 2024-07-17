import sys
from collections import defaultdict


def logger_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            print('Sorry this log name not found')
            return
        except FileNotFoundError:
            print('File not found, try another path to file')
            return
        except IndexError:
            print('Please write path to file')
            return
        except TypeError:
            return
    return inner


@logger_error
def parse_log_line(line: str) -> dict:
    all_inform = {}
    x = line.split(' ')
    all_inform['date'], all_inform['time'], all_inform['level'] = x[0], x[1], x[2]
    all_inform['message'] = ' '.join(x[3::]).replace('\n', '')
    return all_inform


@logger_error
def load_logs(file_path: str) -> list:
    with open(file_path, 'r+') as fh:
        res = [parse_log_line(i) for i in fh.readlines() if i != '\n']
    return res


@logger_error
def filter_logs_by_level(logs: list, level: str) -> list:
    r = []
    if any(i for i in logs if i['level'] == level.upper()):
        for i in logs:
            if i["level"] == level.upper():
                r.append('{} {} {} {}'.format(
                    i["date"], i['time'], i['level'], i['message']))
        print("Деталі логів для рівня 'ERROR':")
        return r
    else:
        raise KeyError


@ logger_error
def count_logs_by_level(logs: list) -> dict:
    count_level = defaultdict(dict)
    for key in logs:
        val = key["level"]
        if count_level[val]:
            count_level[val] += 1
        else:
            count_level[val] = 1
    return count_level


@ logger_error
def display_log_counts(counts: dict):
    header = "Рівень логування | Кількість"
    separator = "-" * len(header)

    table = [header, separator]

    for level, count in counts.items():
        row = f"{level:<16} | {count}"
        table.append(row)

    for row in table:
        print(row)


@ logger_error
def main():
    len_cmd = len(sys.argv)
    load = load_logs(sys.argv[1])
    if any(load):
        if len_cmd >= 2:
            res_dict = count_logs_by_level(load)
            display_log_counts(res_dict)
            if len_cmd >= 3:
                filt = filter_logs_by_level(load, sys.argv[2])
                if filt:
                    for i in filt:
                        print(i)
    else:
        print('Your file is empty')


if __name__ == '__main__':
    main()
