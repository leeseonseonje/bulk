from enum import Enum

from src.main.app.util.random.column_generator import *


class DataType(Enum):
    INTEGER = ('int', 'bigint',)
    REAL_NUMBER = ('decimal', 'float', 'double')
    STRING = ('char', 'varchar', 'text', 'longtext', 'name')
    DATE = ('date', 'datetime', 'timestamp')
    TIME = 'time'
    BOOLEAN = ('tinyint', 'boolean', 'bit')

    @staticmethod
    def type_checking_and_value_generate(data_type, data, n, is_unique):
        if get_data_type(data_type) in DataType.INTEGER.value:
            data.append(str(get_integer(n, is_unique)))
        elif get_data_type(data_type) in DataType.REAL_NUMBER.value:
            length = get_length(data_type)
            data.append(f"'{str(get_string(length, n, is_unique))}'")
        elif get_data_type(data_type) in DataType.STRING.value:
            length = get_length(data_type)
            data.append(f"'{str(get_string(length, n, is_unique))}'")
        elif get_data_type(data_type) in DataType.DATE.value:
            data.append(f"'{str(get_date(is_unique))}'")
        elif get_data_type(data_type) in DataType.TIME.value:
            data.append(f"'{str(get_time(is_unique))}'")
        elif get_data_type(data_type) in DataType.BOOLEAN.value:
            data.append(f"'{str(get_boolean())}'")


def get_data_type(data_type):
    return str(data_type).split('(')[0]


def get_length(data_type):
    split = str(data_type).split('(')
    length = split[1].split(')')
    return int(length[0])


