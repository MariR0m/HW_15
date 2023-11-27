import argparse
from datetime import datetime

from task_1 import get_date, WEEKDAYS, MONTH, Tex


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем дату из строки')
    parser.add_argument('--count', default='1')
    parser.add_argument('--weekday', default=datetime.now().weekday())
    parser.add_argument('--month', default=datetime.now().month)
    args = parser.parse_args()
    print(args)
    return get_date(Tex)


if __name__ == '__main__':
    parser_func()
