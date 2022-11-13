from query_filters import filter_data, map_data, unique_data, sorted_data, limit_data, regex_data
from typing import List, Generator

FILE_NAME = 'data/apache_logs.txt'

CMD_TO_FUNCTION = {
    "filter": filter_data,
    "map": map_data,
    "unique": unique_data,
    "sort": sorted_data,
    "limit": limit_data,
    "regex": regex_data
}


def iter_file(data) -> Generator:
    with open(data) as file:
        for line in file:
            yield line


def query_builder(cmd, value, data) -> List[str]:
    if data is None:
        read_file = iter_file(FILE_NAME)
    else:
        read_file = data
    res = CMD_TO_FUNCTION[cmd](param=value, data=read_file)
    return list(res)





