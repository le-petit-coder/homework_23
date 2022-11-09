import re
from typing import Generator, Set, List


def filter_data(param: str, data: str):
    return filter(lambda x: param in x, data)


def map_data(param: int, data: str):
    number_colom = int(param)
    return map(lambda x: x.split(' ')[number_colom], data)


def unique_data(data: str, param = None) -> Set:
    return set(data)


def sorted_data(param: str, data: str) -> List:
    return sorted(data, reverse=param == 'desc')


def limit_data(param: str, data: str) -> List:
    limit_num = int(param)
    return list(data)[:limit_num]


def regex_data(pattern, data):
    regex = re.compile(pattern)
    return regex.findall(data)
